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
Setting up the database folder is an essential step in ensuring the smooth functioning of the Biomedical Q&A with Language Models project. With Firebase integration in place, storing and managing responses becomes streamlined. Here's how you can set up the database folder:

1. ## Firebase Configuration 
   * Begin by configuring Firebase with the necessary credentials. 
   * Ensure you have the API key, authentication domain, database URL, project ID, storage bucket, messaging sender ID, and app ID handy. 
   * These details are vital for initializing Firebase and establishing a connection with the database.

2. ## Initialize Firebase 
   * Once you have the configuration parameters, initialize Firebase using the pyrebase library. 
   * This step establishes a connection to the Firebase project, enabling interaction with the database.

3. ## Access Authentication 
   * If your project requires authentication for accessing the database, you can utilize Firebase's authentication functionality. 
   * This ensures that only authorized users can perform operations like reading and writing data to the database.

4. ## Database Interaction 
   * With Firebase initialized, you can now interact with the database.
   * In the provided code, a Firebase database instance (db) is created, allowing you to push responses to the database.
   * Each response is stored as a new entry under the "responses" node, containing the question and corresponding answer.
     
## Running the Scripts
* Now that you've set up your environment and installed the necessary packages, you can run the app.py scripts.
* Run the script app.py to fetch responses from PubMed for users query and store it in Firebase.
##
      python app.py

## Usage
* app.py: To fetch responses from PubMed for users query and store it in Firebase.

## License
This project is licensed under the MIT License. You can find more details in the LICENSE file included in the repository.

That's it! You're now ready to retrieve and store biomedical literatures using the provided scripts. If you have any questions or encounter any issues, feel free to reach out to the project maintainers. 
Happy face detecting and recognizing!
