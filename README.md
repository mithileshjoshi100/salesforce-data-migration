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
1. Open the terminal/powershell in the project folder and run the command:✅<br>
    ```
    python main.py
    ```

2. Click on Locate Creads then update creds json files, <br>
 For data extraction, utilize the `old_org_credentials.json` file, <br>
For data insertion, make use of the `new_org_credentials.json` file<br>
Right-click on the file and open it using Notepad (double-clicking will not work). Edit the contents as needed, and don't forget to save the changes.

3.  Click on Open Users :
    update the file [user_emails.py](app/data_extraction/user_emails.py)

4. Close the application and open again using command on terminal:
    ```
    python main.py
    ```
5. If the script fails for any reason, you will receive an error message on the terminal/cmd. Check the type of exception and the accompanying message. For more detailed information, click the "Show Logs" button to access the frequent errors and logs.

6.  If there are no errors displayed on the terminal/cmd, it indicates that the execution of the script has been completed successfully.
7. You can locate the extracted/new file by clicking the "Show Files" button.

8. After closing the application,you can press `ctr+c` to kill process on terminal and close the application from taskbar.

9. Go Slow  !!

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
1. pandas.errors.EmptyDataError: <br>
 No columns to parse from file when csv file is empty

2. simple_salesforce.exceptions.SalesforceAuthenticationFailed: <br>
Internet connection or VPN or Username password 

3. simple_salesforce.exceptions.SalesforceMalformedRequest: <br>
Insertion Failed because of Custom Validation (Handled by Salesfore)


### How to extend script
## simple chnages:
1. changes in query:
    we can happyly add or remove fileds from query unless that filed is dependend on any other object.
    to make change modifly query in the file
    ``salesforce_data_migration/app/data_extraction/query_strings.py``

2. add new object to extract
    steps
    1. add query in the query file
    ``salesforce_data_migration/app/data_extraction/query_strings.py``

        create new variable and store query
        ex: 
        ```Python
        demoobj_query = """
        SELECT id,chiled_obje1__c,filed1,filed2,email
        FROM DEMOObj__c
        WHERE email in {keys}
        """
        ```


    2. add function in extraction file
    ``salesforce_data_migration/app/data_extraction/extraction..py``
    <br>let we have a object with same DEMOObj__c  the the new fucntion will looks like below

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

    3. Update `magic_string.py`
        ```Python
        extraction_objects = [
            ...,
            "DEMOObj__c",
        ]
        ```
    4. Update ``call_api.py``
        ```Python
        def _call(script,object):
            if script == 'EXTRACT':
                import app.data_extraction.extraction as extract
                ...

                 if object == 'DEMOObj__c':
                    logging.info('Started Exicutation for {object}')
                    extract.fetch_demoobj()
                    logging.info('END Exicutation for {object}') 
                ...
        
        ```
        Extraction Script Added 🥳
    
    5. Update [insertion.py](app/data_insertion/insertion.py)
        ```Python
        @lib.log_function_execution
        def insert_demoobj():
            """
            Object Name : DEMOObj__c
            """
            imort_file_path = import_path('df_demoobj.csv')
            export_file_path = export_path('df_demoobj.csv')
            object_dataframe = pd.read_csv(imort_file_path)
            object_dataframe = object_dataframe.fillna('')

            # lookup and update contact related to user
            ## this chiled_obje1 should be inserted before DEMOObj__c
            df_lookup_path = export_path('df_chiled_obje1.csv')
            df_lookup = pd.read_csv(df_lookup_path)
            object_dataframe = lib.vlookup_id(object_dataframe,df_lookup,'chiled_obje1__c')

            # insert the records
            for index, row in object_dataframe.iterrows():
                record = lib.filter_record(row) ## 
                inserted_record = sf.User.create(record)
                object_dataframe.at[index, 'new_Id'] = inserted_record['id']
            
            # export file
            object_dataframe.to_csv(export_file_path, index=False)
        ```

    6. Update `magic_string.py`
        ```Python
        insertion_objects = [
            ...,
            "DEMOObj__c",
        ]
        ```
    7. Update ``call_api.py``
        ```Python
        def _call(script,object):
            if script == 'INSERT':
                import app.data_insertion.insertion as insertion
                ...

                 if object == 'DEMOObj__c':
                    logging.info('Started Exicutation for {object}')
                    insertion.insert_users()
                    logging.info('END Exicutation for {object}') 
                ...
        
        ```

        Insertion Script Added 🥳

