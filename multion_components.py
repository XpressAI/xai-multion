from xai_components.base import InArg, OutArg, InCompArg, Component, BaseComponent, xai_component
import multion
import time
import os



@xai_component
class MultiOnLogin(Component):
    def execute(self, ctx):
        ctx['_multion'] = multion.multion._multion_instance
        if os.path.exists('multion_token.txt'):
            # If it does, read the file
            with open('multion_token.txt', 'r') as file:
                token_content = file.read().strip()
                # Set the token as a dictionary
                ctx['_multion'].token = {'access_token': token_content}
            time.sleep(5)
        else:
            multion.login()
            print("Sleeping until multion_token.txt exists.")
            while not os.path.exists('multion_token.txt'):
                time.sleep(1)

        
@xai_component
class MultiOnNewSession(Component):
    input_prompt: InCompArg[str]
    url: InCompArg[str]
    
    tab_id: OutArg[int]
    out_url: OutArg[str]
        
    def execute(self, ctx):
        response = multion.new_session({
            "input": self.input_prompt.value,
            "url": self.url.value
        })
        self.tab_id.value = int(response['tabId'])
        self.out_url.value = response['url']


@xai_component
class MultiOnUpdateSession(Component):
    input_prompt: InCompArg[str]
    url: InCompArg[str]
    tab_id: InCompArg[int]
        
    out_url: OutArg[str]
    screenshot: OutArg[str]
    message: OutArg[str]
    status: OutArg[str]
        
    def execute(self, ctx):        
        response = multion.update_session(self.tab_id.value, {
            "input": self.input_prompt.value, 
            "url": self.url.value
        })
        
        self.out_url.value = response['url']
        self.screenshot.value = response['screenshot']
        self.message.value = response['message']
        self.status.value = response['status']


        
@xai_component
class MultiOnAutoRun(Component):
    input_prompt: InCompArg[str]
    url: InCompArg[str]
        
    out_url: OutArg[str]
    screenshot: OutArg[str]
    message: OutArg[str]
    status: OutArg[str]
        
    def execute(self, ctx):  
        response = multion.new_session({
            "input": self.input_prompt.value,
            "url": self.url.value
        })
            
        tab_id = int(response['tabId'])
        
        status = response['status']
        
        tries = 0
        while status == 'CONTINUE' and tries < 10:
            response = multion.update_session(tab_id, {
                "input": self.input_prompt.value + response['message'], 
                "url": response['url']
            })
            
            status = response['status']
        
            self.out_url.value = response['url']
            self.screenshot.value = response['screenshot']
            self.message.value = response['message']
            self.status.value = response['status']
            
            tries += 1
