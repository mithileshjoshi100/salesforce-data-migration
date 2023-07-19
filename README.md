## Python Installetion steps 🐍
Download Python installer: Visit the official Python website (https://www.python.org/downloads/) an
1. Download Python installer: Visit the official Python website (https://www.python.org/downloads/) and download the latest stable version of Python for your operating system. Choose either Python 3.x or Python 2.x (Note: Python 2 is no longer actively maintained, so it is recommended to use Python 3).

2. Run the installer: Once the download is complete, run the Python installer. Follow the instructions provided by the installer to install Python on your system.

3. Add Python to PATH (Windows only): During the installation, you might see an option to "Add Python x.x to PATH." Make sure to check this option, as it allows you to use Python from the command prompt or terminal without specifying the full path.

4. Verify the installation: After the installation is complete, open a new command prompt (Windows) or terminal (macOS/Linux) and type:
    ```
    python --version
    ```

    It should display the Python version you installed. Additionally, you can type python and press Enter to enter the Python interactive shell.



## One-time setup ✅
1. Install Python 🐍
2. Open the project folder 📂
3. Open the terminal/powershell in the project folder and run the command:

    ```
    pip install -r requirements.txt
    ```
4. Done with setup!! 🎉

## How to use 🚀
1. Verify credentials in the file: config\credentials\ ✅<br>
```\config\credentials\```
2. Add user emails in the python file: app\data_extraction\user_emails.py  ✉️<br>```app\data_extraction\user_emails.py```
3. Open the terminal/powershell in the project folder and run the command:
    ```
    python main_gui.py
    ```
4. Check logs here (clear old logs before fresh execution): 📜<br>
    ``logs\basic.log``
5. Trace data files: <br>
    Extracted files: ``data\extraction_data`` 📂<br>
    Inserted files with new ids: ``data\insertion_data`` 📂

Feel free to connect if you have any questions! 🤗






## script is redy to user for following objects

1. Contact
2. User
3. PermissionSetAssignment
4. GEIDP_Customer_App_Role_Access__c
5. Contact_Additional_Information__c
6. GEIDPUsersFromManualRegFlow__c
7. GEIDP_Entitled_Feature__c




### Project Structure
```
salesforce_data_migration/
    ├── app/
    │   ├── __init__.py
    │   ├── gui/
    │   │   └── __init__.py
    |   |   └── call_api.py
    |   |   └── magic_strings.py
    |   |   └── run.py
    │   ├── data_extraction/
    │   │   ├── __init__.py
    │   │   └── extraction.py
    │   ├── data_insertion/
    │   │   ├── __init__.py
    │   │   └── insertion.py
    │   └── utils/
    │       ├── __init__.py
    │       └── lib.py
    ├── data/
    │   ├── extraction_data/
    │   │   ├── *.csv
    │   │   └── ...
    │   └── insertion_data/
    │       ├── *.csv
    │       └── ...
    ├── logs/
    │   ├── extraction.log
    │   └──insertion.log
    ├── tests/
    │   ├── __init__.py
    │   ├── test_lib.py
    │   └── ...
    ├── config/
    │   ├── credentials/
    │   │    ├── new_org_credentials.json
    │   │    └── old_org_credentials.json
    │   ├── __init__.py
    │   ├── config.py
    │   └── ...
    ├── docs/
    ├── requirements.txt
    ├── README.md
    ├── LICENSE
    ├── requirements.txt
    └── main.py
```

### Possible Errors :
1. pandas.errors.EmptyDataError: No columns to parse from file
wh en csv file is empty

### How to extend script
## simple chnages:
1. changes in query:
    we can happyly add or remove fileds from query unless that filed is dependend on any other object.
    to make change modifly query in the file
    ``salesforce_data_migration/app/data_extraction/query_strings.py``
2. add new object to extract
    steps
    1. add query in the query file
    ``path to query file``
    2. add function in extraction file
    ``path to extraction file``
    let we have a object with same DEMOObj__c  the the new fucntion will looks like below
    ```Python
    @lib.log_function_execution
    def fetch_demoobj():
        """
        Object Name : DEMOObj__c
        """
        sf_connection = sf  
        query = query_strings.demoobj_query 
        email_keys = user_emails.emails 
        file_name = export_path('df_demoobj.csv')

        response = lib.execute_soql_query(sf_connection, query,  keys=email_keys)
        contact_dataframe = lib.api_response_to_dataframe(response)
        contact_dataframe.to_csv(file_name, index=False)

    ```

