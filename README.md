## Augmented Question-Answering System for Biomedical Literature Retrieval using LLM and PubMed

## Overview
The Biomedical Q&A with Language Models project is an innovative approach to accessing and understanding vast amounts of biomedical literature using state-of-the-art language models. Leveraging advanced natural language processing (NLP) techniques, this project enables users to ask questions about various biomedical topics and receive accurate and relevant answers in real-time.

## Table of Contents
1. [Description](#Description)
2. [Prerequisites](#Prerequisites)
3. [Setting up the Environment](#SettinguptheEnvironment)
4. [Setting up the Database Folder](#SettinguptheDatabaseFolder)
5. [Running the Scripts](#RunningtheScripts)
6. [Usage](#Usage)
7. [License](#License)

## Description
The Biomedical Q&A with Language Models project is a cutting-edge solution designed to facilitate easy access to biomedical information. By combining advanced language models with integration capabilities with PubMed, users can simply input their queries into the Streamlit interface and receive accurate, evidence-based responses in real-time. The system also incorporates features like face detection and recognition, ensuring a comprehensive user experience. With its ability to fetch relevant articles from PubMed, interact with powerful language models, and store responses for future reference, this project represents a significant advancement in biomedical research and information retrieval.

## Prerequisites
Before you can start using the face detection and recognition scripts, make sure you have the following prerequisites installed on your system:

1. ## Python:
    * Python is the programming language used for this project. If you don't have Python installed on your system, you can download and install it from here.

2. ## Visual Studio C++ Build Tools:
   * These tools are necessary for compiling certain dependencies required by the libraries used in this project. Follow the steps below to download and install
     Visual Studio along with the required workload for "Desktop Development with C++":

   ## Step 1: Download Visual Studio
      * Navigate to Visual Studio Downloads website.
      * Click on the "Download Visual Studio" button.
      * Follow the on-screen instructions to download the Visual Studio installer.
      * Once the installer is downloaded, run it.
        
   ## Step 2: Download and install the workload: "Desktop Development with C++"
      * Open the Visual Studio Installer.
      * Select "Visual Studio C++ Build Tools" from the list of available products.
      * Click on "Install" to download and install the workload.
      * Follow the on-screen instructions to complete the installation.
      
   ## Step 3: Customize Installation (Optional)
      * If you want to customize the installation or select additional components, you can do so by clicking on the "Individual components" tab.
      * Here, you can browse and select additional components based on your requirements.
      
   ## Step 4: Install
      * After selecting the desired workload and components, click on the "Install" button to begin the installation process.
      * Follow the on-screen instructions to complete the installation.

   ## Setting up the Environment
    * To ensure a smooth running of the scripts, it's recommended to set up a Python virtual environment. Follow these steps to create the environment:

1. ## Create a Python Environment:
      * Open your terminal or command prompt and navigate to your project directory.
      * Run the following command to create a virtual environment named myenv:
##
    python -m venv myenv
    
2. ## Activate the Environment:

      * Depending on your operating system, use the appropriate command to activate the virtual environment:
  On Windows:
  ##
    myenv\Scripts\activate
  On macOS/Linux:
  ##
    source myenv/bin/activate
    
3. ## Install Necessary Packages:

      * Once the virtual environment is activated, install the required packages using pip:
  ##
    pip install -r requirements.txt

## Setting up the Database Folder
