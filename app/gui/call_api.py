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


def _call(script,object):
    if script == 'EXTRACT':
        import app.data_extraction.extraction as extract
        if object == 'Contact':
            print('call contact extract')
            extract.fetch_contacts()
            pass
        if object == 'User':
            extract.fetch_users()
            pass
        if object == 'PermissionSetAssignment':
            extract.fetch_permission_set_assignment()

            pass
        if object == 'GEIDP_Customer_App_Role_Access__c':
            extract.fetch_app_role_access()
            pass
        if object == 'Contact_Additional_Information__c':
            extract.fetch_contact_additional_information()
            pass
        if object == 'GEIDPUsersFromManualRegFlow__c':
            extract.fetch_umr()
            pass
        if object == 'GEIDP_Entitled_Feature__c':
            extract.fetch_geidp_entitled_feature()
            pass
        if object == 'ALL OBJECTS':
            extract.fetch_contacts()
            extract.fetch_users()
            extract.fetch_permission_set_assignment()
            extract.fetch_app_role_access()
            extract.fetch_contact_additional_information()
            extract.fetch_umr()
            extract.fetch_geidp_entitled_feature()
            pass

    if script == 'INSERT':
        import app.data_insertion.insertion as insertion
        if object == 'Contact':
            insertion.insert_contact()
            pass
        if object == 'User':
            insertion.insert_users()
            pass
        if object == 'PermissionSetAssignment':
            insertion.insert_psa()
            pass
        if object == 'GEIDP_Customer_App_Role_Access__c':
            insertion.insert_approllaccess()
            pass
        if object == 'Contact_Additional_Information__c':
            insertion.insert_contact_additional_information()
            pass
        if object == 'GEIDPUsersFromManualRegFlow__c':
            insertion.insert_umr()
            pass
        if object == 'GEIDP_Entitled_Feature__c':
            insertion.insert_geidp_entitled_feature()
            pass
        