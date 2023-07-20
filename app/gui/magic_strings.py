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
text2 = 'Click on Locate Creads :\n \tupdate creds json files'
text3 = 'Click on Locate Users :\n \tupdate user_emails.py'
text4 = 'Restart the application'
text5 = 'Select Script Type'
text6 = 'Select Object'
text7 = 'Click on Execute Script'
text8 = 'check logs and files'
text9 = 'Go slow!!!'

text_lst = [text1,text2,text3,text4,text5,text6,text7,text8,text9]