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


import logging
import app.utils.lib as lib
import config.config as config
import pandas as pd

sf = config.connect("new_org")
import_path = lambda s:f'data/extraction_data/{s}'
export_path = lambda s:f'data/insertion_data/{s}'


@lib.log_function_execution
def insert_contact():
    """
    Object Name : Contact
    """
    imort_file_path = import_path('df_contact.csv')
    export_file_path = export_path('df_contact.csv')
    object_dataframe = pd.read_csv(imort_file_path)
    object_dataframe = object_dataframe.fillna('')

    for index, row in object_dataframe.iterrows():
        record = lib.filter_record(row) ## 
        inserted_record = sf.Contact.create(record)
        object_dataframe.at[index, 'new_Id'] = inserted_record['id']
    
    object_dataframe.to_csv(export_file_path, index=False)


@lib.log_function_execution
def insert_users():
    """
    Object Name : User
    """
    imort_file_path = import_path('df_user.csv')
    export_file_path = export_path('df_user.csv')
    object_dataframe = pd.read_csv(imort_file_path)
    object_dataframe = object_dataframe.fillna('')

    # lookup and update contact related to user
    df_lookup_path = export_path('df_contact.csv')
    df_lookup = pd.read_csv(df_lookup_path)
    object_dataframe = lib.vlookup_id(object_dataframe,df_lookup,'ContactId')

    # insert the records
    for index, row in object_dataframe.iterrows():
        record = lib.filter_record(row) ## 
        inserted_record = sf.User.create(record)
        object_dataframe.at[index, 'new_Id'] = inserted_record['id']
    
    # export file
    object_dataframe.to_csv(export_file_path, index=False)


@lib.log_function_execution
def insert_psa():
    """
    Object Name : PermissionSetAssignment
    """
    imort_file_path = import_path('df_psa.csv')
    export_file_path = export_path('df_psa.csv')
    object_dataframe = pd.read_csv(imort_file_path)
    object_dataframe = object_dataframe.fillna('')

    # lookup and update AssigneeId related to psa
    df_lookup_path = export_path('df_user.csv')
    df_lookup = pd.read_csv(df_lookup_path)
    object_dataframe = lib.vlookup_id(object_dataframe,df_lookup,'AssigneeId')

    # insert the records
    for index, row in object_dataframe.iterrows():
        record = lib.filter_record(row)
        try:
            inserted_psa = sf.PermissionSetAssignment.create(record)
            object_dataframe.at[index, 'new_Id'] = inserted_psa['id']
        except:
            object_dataframe.at[index, 'new_Id'] = '######'
    
    # export file
    object_dataframe.to_csv(export_file_path, index=False)


@lib.log_function_execution
def insert_approllaccess():
    """
    Object Name : GEIDP_Customer_App_Role_Access__c
    """
    imort_file_path = import_path('df_approllaccess.csv')
    export_file_path = export_path('df_approllaccess.csv')
    object_dataframe = pd.read_csv(imort_file_path)
    object_dataframe = object_dataframe.fillna('')

    df_lookup_path = export_path('df_user.csv')
    df_lookup = pd.read_csv(df_lookup_path)
    object_dataframe = lib.vlookup_id(object_dataframe,df_lookup,'UserID__c')

    df_lookup_path = export_path('df_contact.csv')
    df_lookup = pd.read_csv(df_lookup_path)
    object_dataframe = lib.vlookup_id(object_dataframe,df_lookup,'Contact__c')

    # insert the records
    for index, row in object_dataframe.iterrows():
        record = lib.filter_record(row)
        inserted_psa = sf.GEIDP_Customer_App_Role_Access__c.create(record)
        object_dataframe.at[index, 'new_Id'] = inserted_psa['id']

    # export file
    object_dataframe.to_csv(export_file_path, index=False)
    

@lib.log_function_execution
def insert_contact_additional_information():
    """
    Object Name : Contact_Additional_Information__c
    """
    imort_file_path = import_path('df_cai.csv')
    export_file_path = export_path('df_cai.csv')
    object_dataframe = pd.read_csv(imort_file_path)
    object_dataframe = object_dataframe.fillna('')

    df_lookup_path = export_path('df_contact.csv')
    df_lookup = pd.read_csv(df_lookup_path)
    object_dataframe = lib.vlookup_id(object_dataframe,df_lookup,'Contact__c')

    # insert the records
    for index, row in object_dataframe.iterrows():
        record = lib.filter_record(row)
        inserted_psa = sf.Contact_Additional_Information__c.create(record)
        object_dataframe.at[index, 'new_Id'] = inserted_psa['id']

    # export file
    object_dataframe.to_csv(export_file_path, index=False)


@lib.log_function_execution
def insert_umr():
    """
    Object Name : GEIDPUsersFromManualRegFlow__c
    """
    imort_file_path = import_path('df_umr.csv')
    export_file_path = export_path('df_umr.csv')
    object_dataframe = pd.read_csv(imort_file_path)
    object_dataframe = object_dataframe.fillna('')

    df_lookup_path = export_path('df_user.csv')
    df_lookup = pd.read_csv(df_lookup_path)
    print(object_dataframe.columns)
    object_dataframe = lib.vlookup_id(object_dataframe,df_lookup,'User__c')

    df_lookup_path = export_path('df_contact.csv')
    df_lookup = pd.read_csv(df_lookup_path)
    object_dataframe = lib.vlookup_id(object_dataframe,df_lookup,'Contact__c')
    
    # insert the records
    for index, row in object_dataframe.iterrows():
        record = lib.filter_record(row)
        inserted_psa = sf.GEIDPUsersFromManualRegFlow__c.create(record)
        object_dataframe.at[index, 'new_Id'] = inserted_psa['id']
    
    # export file
    object_dataframe.to_csv(export_file_path, index=False)
    

@lib.log_function_execution    
def insert_geidp_entitled_feature():
    """
    Object Name : GEIDP_Entitled_Feature__c
    """
    imort_file_path = import_path('df_feature.csv')
    export_file_path = export_path('df_feature.csv')
    object_dataframe = pd.read_csv(imort_file_path)
    object_dataframe = object_dataframe.fillna('')

    df_lookup_path = export_path('df_user.csv')
    df_lookup = pd.read_csv(df_lookup_path)
    object_dataframe = lib.vlookup_id(object_dataframe,df_lookup,'User__c')

    df_lookup_path = export_path('df_contact.csv')
    df_lookup = pd.read_csv(df_lookup_path)
    object_dataframe = lib.vlookup_id(object_dataframe,df_lookup,'Contact__c')

    df_lookup_path = export_path('df_approllaccess.csv')
    df_lookup = pd.read_csv(df_lookup_path)
    object_dataframe = lib.vlookup_id(object_dataframe,df_lookup,
                                      'GEIDP_Customer_App_Role_Access__c')

    # insert the records
    for index, row in object_dataframe.iterrows():
        record = lib.filter_record(row)
        inserted_psa = sf.GEIDP_Entitled_Feature__c.create(record)
        object_dataframe.at[index, 'new_Id'] = inserted_psa['id']

    # export file
    object_dataframe.to_csv(export_file_path, index=False)
    