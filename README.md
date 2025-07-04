# GitHub Copilot Lab

Welcome to the **GitHub Copilot Lab**! This project is designed to help users become familiar with GitHub Copilot, its features, and its capabilities. Whether you are new to Copilot or looking to explore its advanced functionalities, this repository provides a hands-on environment to learn and experiment.

This readme file is itself an excellent example of how using GitHub Copilot can help generate documentation, code snippets, and explanations. As you work through the examples in this repository, you will see how Copilot can assist you.

## Table of Contents
- [Purpose](#purpose)
- [Pre-Requisites](#pre-requisites)
- [Audience](#audience)
- [Using GitHub Copilot](#using-github-copilot)
  - [Choosing a License](#choosing-a-license)
  - [Setting Up GitHub Copilot](#setting-up-github-copilot)
- [Getting Started](#getting-started)
  - [1. GitHub Codespaces (Recommended)](#1-github-codespaces-recommended)
  - [2. Use a Dev Container](#2-use-a-dev-container)
  - [3. Clone Locally](#3-clone-locally)
- [Additional Resources](#additional-resources)
---

## Pre-Requisites
This demo repo will assume that you have the following pre-requisites in place:

- **GitHub Account**: You will need a GitHub account to access Copilot and this repository.
- **GitHub Copilot Access**: Ensure you have access to GitHub Copilot. See section "Using GitHub Copilot" below for details on how to set this up.
- **Development Environment**: You can use any IDE that supports GitHub Copilot, such as Visual Studio Code, JetBrains IDEs, or others. 
--- 

## Audience 
This lab will assume the following:
- You are familiar with the basics of using an IDE (Integrated Development Environment) like Visual Studio Code or JetBrains
- You have at least a basic understanding of using the terminal or command line interface
- You have at least a basic understanding of Python programming, as the examples will be in Python.
---

## Using GitHub Copilot

### Choosing a License
I recommend using a **personal GitHub Copilot license** to run this demo. Your most cost-effictive options include:

- **GitHub Copilot Free**: Available for all, but limited to:
  - 2,000 code completions per month
  - 50 chat requests per month / agent mode requests
  - Access to limited Github Copilot models (GPT, Claude etc.)
- **GitHub Copilot Pro**: Paid subscription with:
  - Unlimited code completions
  - Unlimited chat requests
  - Access to the latest models (GPT-4, Claude 3, etc.)

For those who are not sure what all this mean yet, don't worry! For the purposes of this demo, the **free version** will be sufficient so my suggestion will be to get started with that. 
---

### Setting Up GitHub Copilot
There are multiple options for setting up list lab below under "Getting Started". No matter what option you choose, you will need to perform the following:
1. **Install the GitHub Copilot Extension**:
   - For Visual Studio Code, install the [GitHub Copilot extension](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot).
   - For other IDEs, refer to the specific installation instructions for GitHub Copilot.
   - Options 1 & 2 for "Getting Started" below will do this step for you


2. **Sign In to GitHub**:
   - If using Visual Studio Code, open the Command Palette (`Ctrl+Shift+P`), then type and select `GitHub: Sign in`.
   - This will authenticate your GitHub account and link it to the Copilot extension.
   - For other IDEs, please follow their documentation for signing in to GitHub.
---

## Getting Started
You can start using this repository in several ways:


### Option 1. GitHub Codespaces (Recommended)
If you have access to [GitHub Codespaces](https://github.com/features/codespaces), you can launch this repository directly in the cloud. 

This is recommended as it will provision a pre-configured environment with all necessary tools and extensions that is isolated from your local machine:
   - Click the **Code** button on the repository page and select **Open with Codespaces**.
   - This provides a ready-to-use development environment in your browser.
   - Most personal (free) accounts get around 60 hours of free Codespaces usage per month, which is sufficient for this demo.
---

### Option 2. Use a Dev Container
If you have [Docker](https://www.docker.com/) and the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) installed, open the repository in a dev container:
   - Open the Command Palette (`Ctrl+Shift+P`), then select `Dev Containers: Open Folder in Container...`.
   - This will set up a reproducible development environment.
   ---

### Option 3. Clone Locally
1. Clone the repository to your local machine:
   ```bash
   git clone <repository-url>
   cd demo-github-copilot
   ```
2. Open the folder in [Visual Studio Code](https://code.visualstudio.com/).
3. Make sure you have the [GitHub Copilot extension](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot) installed, as well as a recent version of Python 3.
---

## Additional Resources
- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)

