from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

base_path = os.path.abspath(os.path.dirname(__file__))  # Gets the absolute path of the current script
crx_path = os.path.join(base_path, 'test', 'MultiOnExtension.crx')
# Get environment variables
email = os.getenv('MULTION_EMAIL')
password = os.getenv('MULTION_PASSWORD')

# Setup Chrome options
options = Options()
options.add_argument('--headless')  # Enable headless mode
options.add_argument('--no-sandbox')  # Bypass OS security model
options.add_argument('--disable-dev-shm-usage')  # Overcome limited resource problems
options.add_extension(crx_path)

# Initialize WebDriver
driver = webdriver.Chrome(options=options)

try:
    driver.get('https://platform.multion.ai/login?callbackUrl=https://platform.multion.ai/beta')

    email_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[type="email"]'))
    )
    password_input = driver.find_element(By.CSS_SELECTOR, 'input[type="password"]')

    email_input.send_keys(email)
    password_input.send_keys(password)

    login_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    login_button.click()

    # Handle post-login steps or verifications here

finally:
    # Ensure the browser closes cleanly even if the test fails
    driver.quit()
