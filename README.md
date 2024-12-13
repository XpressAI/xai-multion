<p align="center">
  <a href="https://github.com/XpressAI/xircuits/tree/master/xai_components#xircuits-component-library-list">Component Libraries</a> •
  <a href="https://github.com/XpressAI/xircuits/tree/master/project-templates#xircuits-project-templates-list">Project Templates</a>
  <br>
  <a href="https://xircuits.io/">Docs</a> •
  <a href="https://xircuits.io/docs/Installation">Install</a> •
  <a href="https://xircuits.io/docs/category/tutorials">Tutorials</a> •
  <a href="https://xircuits.io/docs/category/developer-guide">Developer Guides</a> •
  <a href="https://github.com/XpressAI/xircuits/blob/master/CONTRIBUTING.md">Contribute</a> •
  <a href="https://www.xpress.ai/blog/">Blog</a> •
  <a href="https://discord.com/invite/vgEg2ZtxCw">Discord</a>
</p>





<p align="center"><i>Xircuits Component Library to interface with MultiOn! Simplify browsing and session management in your workflows.</i></p>

## Xircuits Component Library for MultiOn

This library enables seamless integration of MultiOn browsing capabilities into your Xircuits workflows. It simplifies session creation, management, and advanced web browsing tasks using MultiOn's powerful API.

## Table of Contents

- [Preview](#preview)
- [Prerequisites](#prerequisites)
- [Main Xircuits Components](#main-xircuits-components)
- [Try the Examples](#try-the-examples)
- [Installation](#installation)

## Preview

### The Example:

<img src="https://github.com/user-attachments/assets/c682ae36-c635-4040-a6e2-0aca513625e3" alt="multion_example _png"/>

### The Result:

<img src="https://github.com/user-attachments/assets/c8f449da-8f97-4d38-9fed-a76537108ea8" alt="multion_example"/>

## Prerequisites

Before you begin, you will need the following:

1. Python3.9+.
2. Xircuits.
3. MultiOn API

## Main Xircuits Components

### MultiOnLogin Component:

Authenticates using an API key and initializes a MultiOn client for session management and browsing tasks.

<img src="https://github.com/user-attachments/assets/9e25ab68-9828-431d-9b1e-9ef6c0cdacc2" alt="MultiOnLogin" width="200" height="75" />

### MultiOnNewSession Component:

Creates a new MultiOn browsing session using a command, URL, and step configurations, while capturing the session's output and metadata.

<img src="https://github.com/user-attachments/assets/f76f5bcf-c323-49c5-a579-5232afdc8159" alt="MultiOnNewSession" width="200" height="200" />

### MultiOnStepSession Component:

Continues a previously started session with a new command, enabling iterative browsing within the same session.

<img src="https://github.com/user-attachments/assets/841b2147-0415-4104-be23-823dd209c253" alt="MultiOnStepSession" width="200" height="200" />

## Try The Examples

We have provided an example workflow to help you get started with the MultiOn component library. Give it a try and see how you can create custom MultiOn components for your applications.

### MultiOn Example  
This example demonstrates how to authenticate with MultiOn using the **MultiOnLogin** component, create a new browsing session with the **MultiOnNewSession** component, and retrieve the session's output. The workflow navigates to Google, runs a query, and prints the screenshot URL and output message.
## Installation
To use this component library, ensure that you have an existing [Xircuits setup](https://xircuits.io/docs/main/Installation). You can then install the MultiOn library using the [component library interface](https://xircuits.io/docs/component-library/installation#installation-using-the-xircuits-library-interface), or through the CLI using:

```
xircuits install multion
```
You can also do it manually by cloning and installing it:
```
# base Xircuits directory
git clone https://github.com/XpressAI/xai-multion xai_components/xai_multion
pip install -r xai_components/xai_multion/requirements.txt 
```