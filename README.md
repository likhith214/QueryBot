
### Setting Up and Running ImarticusBot in VSCode

#### Step 1: Install Required Packages
First, open your Python interpreter in the PowerShell terminal within VSCode and type the following command to install the necessary packages:
```sh
pip install streamlit streamlit-chat langchain transformers googlesearch-python
```

#### Step 2: Obtain API Key from Hugging Face
Since we are working with an API, you'll need to obtain an API key from Hugging Face. Follow these steps:

1. **Sign Up:**
   - Go to [Hugging Face](https://huggingface.co/join) and sign up for an account.

2. **Generate Access Token:**
   - Click on your profile image in the top right corner and select the "Settings" option.
   - From the options on the left, select "Access Tokens."
   - Click on "New Token," name your token, and set the "Role" to "Read."
   - Click on "Generate a Token" and copy the token for future use.

#### Step 3: Run the Script
To run the script, use the following command in your terminal:
```sh
streamlit run imarticusbot.py
```
Check for any errors. If you encounter a dependency error, resolve it by installing the required package:
```sh
pip install <PackageName>
```
There should be no errors in the code as it runs successfully on my machine.

#### Step 4: Initialize ImarticusBot
After successfully executing the code, a new browser tab will open displaying the bot interface. In the left sidebar, paste your Hugging Face token and press Enter.

#### Step 5: Interact with ImarticusBot
Your ImarticusBot is now ready to rock! Enter your query in the text box to get a response.
