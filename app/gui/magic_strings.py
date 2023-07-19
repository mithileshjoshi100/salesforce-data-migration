### -ACCENTURE CONFIDENTIAL-
### Type: Source Code
###
### Copyright (c) 2023, ACCENTURE
### All Rights Reserved.
###
### This unpublished material is proprietary to ACCENTURE. The methods and
### techniques described herein are considered trade secrets and/or
### confidential. Reproduction or distribution, in whole or in part, is
### forbidden except by express written permission of ACCENTURE.


APP_NAME = 'User Migration Tool'
THEME = 'blue'
MODE = 'Dark'
DEFAULT_SIZE = '800x600'
FONT_NAME = 'Consolas'
SELECT_SCRIPT_LABEL = 'SELECT SCRIPT'
SELECT_OBJECT_LABEL = 'SELECT OBJECT'
RUN_SCRIPT_BTN = 'Execute Script'
SHOW_LOGS_BTN = 'show logs'
SHOW_FILES_BTN = 'show files'
SHOW_USERS_BTN = 'Locate Users'
SHOW_CREDS_BTN = 'Locate Creds'

# DO NOT CHANGE THIS
script_options = [
    'SELECT',
    'EXTRACT',
    'INSERT'
]

default_objects = [
    'SELECT Object'
]

extraction_objects = [
    "Contact",
    "User",
    "PermissionSetAssignment",
    "GEIDP_Customer_App_Role_Access__c",
    "Contact_Additional_Information__c",
    "GEIDPUsersFromManualRegFlow__c",
    "GEIDP_Entitled_Feature__c",
    "ALL OBJECTS"
]

insertion_objects = [
    "Contact",
    "User",
    "PermissionSetAssignment",
    "GEIDP_Customer_App_Role_Access__c",
    "Contact_Additional_Information__c",
    "GEIDPUsersFromManualRegFlow__c",
    "GEIDP_Entitled_Feature__c",
]

text1 = 'STEPS'
text2 = 'Update usre creds in the file \n \\config\\credentials'
text2 = 'For data extraction add user emails to \n \\app\\data_extraction\\user_emails.py'
text3 = 'Must extract the data using \n same tool before insertaion'
text4 = 'if anything fails you will the error \n on output screen'
text5 = 'check logs for flow of exicution'
text6 = 'run the insert scripts in sequence \nchiled records must inserted before perent'
text7 = 'go slow!!!'

text_lst = [text1,text2,text3,text4,text5,text6,text7]