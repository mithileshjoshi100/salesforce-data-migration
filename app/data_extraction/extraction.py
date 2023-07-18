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
import app.data_extraction.query_strings as query_strings
import app.data_extraction.user_emails as user_emails


sf = config.connect("old_org")
export_path = lambda s:f'data/extraction_data/{s}'


@lib.log_function_execution
def fetch_contacts():
    """
    Object Name : Contact
    """
    sf_connection = sf  
    query = query_strings.contact_query 
    email_keys = user_emails.emails 
    file_name = export_path('df_contact.csv')

    response = lib.execute_soql_query(sf_connection, query, keys=email_keys)
    contact_dataframe = lib.api_response_to_dataframe(response)
    contact_dataframe.to_csv(file_name, index=False)


@lib.log_function_execution
def fetch_users():
    """
    Object Name : User
    """
    sf_connection = sf  
    query = query_strings.user_query 
    email_keys = user_emails.emails
    file_name = export_path('df_user.csv')

    response = lib.execute_soql_query(sf_connection, query, keys=email_keys)
    object_dataframe = lib.api_response_to_dataframe(response)
    object_dataframe.to_csv(file_name, index=False)
    

@lib.log_function_execution
def fetch_permission_set_assignment():
    """
    Object Name: PermissionSetAssignment
    """
    sf_connection = sf  
    query = query_strings.permissionsetassignment_query 
    email_keys = user_emails.emails  
    file_name = export_path('df_psa.csv')

    response = lib.execute_soql_query(sf_connection, query, keys=email_keys)
    object_dataframe = lib.api_response_to_dataframe(response)
    object_dataframe.to_csv(file_name, index=False)


@lib.log_function_execution
def fetch_app_role_access():
    """
    Object Name: GEIDP_Customer_App_Role_Access__c 
    """
    sf_connection = sf  
    query = query_strings.customerappaoleaccess_query 
    email_keys = user_emails.emails
    file_name = export_path('df_approllaccess.csv')

    response = lib.execute_soql_query(sf_connection, query, keys=email_keys)
    object_dataframe = lib.api_response_to_dataframe(response)
    object_dataframe.to_csv(file_name, index=False)


@lib.log_function_execution
def fetch_contact_additional_information():
    """
    Object Name: Contact_Additional_Information__c 
    """
    sf_connection = sf  
    query = query_strings.contactadditionalinformation_query 
    email_keys = user_emails.emails
    file_name = export_path('df_cai.csv')

    response = lib.execute_soql_query(sf_connection, query, keys=email_keys)
    object_dataframe = lib.api_response_to_dataframe(response)
    object_dataframe.to_csv(file_name, index=False)


@lib.log_function_execution
def fetch_umr():
    """
    Object Name: GEIDPUsersFromManualRegFlow__c 
    """
    sf_connection = sf  
    query = query_strings.usersfrommanualregflow_query 
    email_keys = user_emails.emails
    file_name = export_path('df_umr.csv') 

    response = lib.execute_soql_query(sf_connection, query, keys=email_keys)
    object_dataframe = lib.api_response_to_dataframe(response)
    object_dataframe.to_csv(file_name, index=False)


@lib.log_function_execution
def fetch_geidp_entitled_feature():
    """
    Object Name: GEIDP_Entitled_Feature__c 
    """
    sf_connection = sf  
    query = query_strings.geidpentitledfeature_query 
    email_keys = user_emails.emails 
    file_name = export_path('df_feature.csv')

    response = lib.execute_soql_query(sf_connection, query, keys=email_keys)
    object_dataframe = lib.api_response_to_dataframe(response)
    object_dataframe.to_csv(file_name, index=False)

