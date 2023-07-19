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

def _call(script,object):
    if script == 'EXTRACT':
        import app.data_extraction.extraction as extract
        if object == 'Contact':
            logging.info('Started Exicutation for {object}')
            extract.fetch_contacts()
            logging.info('END Exicutation for {object}')
            
        if object == 'User':
            logging.info('Started Exicutation for {object}')
            extract.fetch_users()
            
        if object == 'PermissionSetAssignment':
            logging.info('Started Exicutation for {object}')
            extract.fetch_permission_set_assignment()
            logging.info('END Exicutation for {object}')

        if object == 'GEIDP_Customer_App_Role_Access__c':
            logging.info('Started Exicutation for {object}')
            extract.fetch_app_role_access()
            logging.info('END Exicutation for {object}')
            
        if object == 'Contact_Additional_Information__c':
            logging.info('Started Exicutation for {object}')
            extract.fetch_contact_additional_information()
            logging.info('END Exicutation for {object}')
            
        if object == 'GEIDPUsersFromManualRegFlow__c':
            logging.info('Started Exicutation for {object}')
            extract.fetch_umr()
            logging.info('END Exicutation for {object}')
            
        if object == 'GEIDP_Entitled_Feature__c':
            logging.info('Started Exicutation for {object}')
            extract.fetch_geidp_entitled_feature()
            logging.info('END Exicutation for {object}')
            
        if object == 'ALL OBJECTS':
            logging.info('Started Exicutation for {object}')
            extract.fetch_contacts()
            extract.fetch_users()
            extract.fetch_permission_set_assignment()
            extract.fetch_app_role_access()
            extract.fetch_contact_additional_information()
            extract.fetch_umr()
            extract.fetch_geidp_entitled_feature()
            logging.info('END Exicutation for {object}')
            pass

    if script == 'INSERT':
        import app.data_insertion.insertion as insertion
        if object == 'Contact':
            logging.info('Started Exicutation for {object}')
            insertion.insert_contact()
            logging.info('END Exicutation for {object}')
            
        if object == 'User':
            logging.info('Started Exicutation for {object}')
            insertion.insert_users()
            logging.info('END Exicutation for {object}')
            
        if object == 'PermissionSetAssignment':
            logging.info('Started Exicutation for {object}')
            insertion.insert_psa()
            logging.info('END Exicutation for {object}')
            
        if object == 'GEIDP_Customer_App_Role_Access__c':
            logging.info('Started Exicutation for {object}')
            insertion.insert_approllaccess()
            logging.info('END Exicutation for {object}')
            
        if object == 'Contact_Additional_Information__c':
            logging.info('Started Exicutation for {object}')
            insertion.insert_contact_additional_information()
            logging.info('END Exicutation for {object}')
            
        if object == 'GEIDPUsersFromManualRegFlow__c':
            logging.info('Started Exicutation for {object}')
            insertion.insert_umr()
            logging.info('END Exicutation for {object}')
            
        if object == 'GEIDP_Entitled_Feature__c':
            logging.info('Started Exicutation for {object}')
            insertion.insert_geidp_entitled_feature()
            logging.info('END Exicutation for {object}')
            
        