# To use the Salesforce Data Migration Python project, follow these steps:



1. Check for existing Python installation (optional): Before installing Python, check if it is already installed on your system. Open a command prompt (Windows) or terminal (macOS/Linux) and type:
    ```python --version```

    If Python is installed, it will display the version number. If not, proceed with the installation steps below.

## Python Installetion steps
1. Download Python installer: Visit the official Python website (https://www.python.org/downloads/) and download the latest stable version of Python for your operating system. Choose either Python 3.x or Python 2.x (Note: Python 2 is no longer actively maintained, so it is recommended to use Python 3).

2. Run the installer: Once the download is complete, run the Python installer. Follow the instructions provided by the installer to install Python on your system.

3. Add Python to PATH (Windows only): During the installation, you might see an option to "Add Python x.x to PATH." Make sure to check this option, as it allows you to use Python from the command prompt or terminal without specifying the full path.

4. Verify the installation: After the installation is complete, open a new command prompt (Windows) or terminal (macOS/Linux) and type:
    ```
    python --version
    ```

    It should display the Python version you installed. Additionally, you can type python and press Enter to enter the Python interactive shell.

## Get back with user migration project
With Python installed, you can now proceed with the steps mentioned to use the Salesforce Data Migration Python project. Install the required dependencies using pip, set up credentials in the config.json file, and run the Python script to perform the data migration.

1. Install dependencies: Navigate to the project folder and install the required Python dependencies using pip:

    ``refer the structure.txt file for project tree``

    Remember to install the required dependencies by running:
    ```
    cd salesforce-data-migration  
    pip install -r requirements.txt
    ```

    If you encounter any issues during the installation, refer to the Python documentation or seek assistance from the Python community for troubleshooting.


2. Set up credentials: Create a config.json file in the root folder to store your Salesforce credentials. The file should have the following structure:
    ```
    {
        "old_org": {
            "username": "your_old_org_username",
            "password": "your_old_org_password",
            "security_token": "your_security_token",
            "domain": "test"
        },
        "new_org": {
            "username": "your_new_org_username",
            "password": "your_new_org_password",
            "security_token": "your_security_token",
            "domain": "test"
        }
    }
    ```

3. Configure SOQL query (if required to update): In your Python script, define your SOQL query based on your requirements. For example:
``salesforce_data_migration/data_extraction/query_strings.py``
   



4. Run the script: Execute your Python main.py script to run the data migration. 
    ```
    python main.py
    ```

5. Check logs and results: The script will log its progress and any errors encountered during execution. The log file application.log will be generated in the root folder.


Please note that this is a high-level guide, and you may need to customize the project to fit your specific Salesforce data migration needs. Adjust the SOQL query, data handling, and Salesforce API interactions according to your requirements.