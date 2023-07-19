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


import json
import os
import simple_salesforce
import logging


def connect(org_name):
    """
    Connects to a Salesforce organization using the provided credentials.

    Args:
        org_name (str): The name of the organization.

    Returns:
        simple_salesforce.Salesforce: An instance of the simple_salesforce.
        Salesforce class representing the connection 
        to the Salesforce organization.

    Raises:
        FileNotFoundError: 
        If the credentials file for the specified organization does 
        not exist.

        simple_salesforce.exceptions.SalesforceAuthenticationFailed:
        If the credentials is wrong or the network problem or VPN problem.

    Example:
        To connect to a new organization:

        >>> sf_new_org = connect("new_org")
        
        To connect to an existing organization:

        >>> sf_old_org = connect("old_org")
    """

    file_path = os.path.join(
        os.path.dirname(__file__), 
        'credentials',
        f'{org_name}_credentials.json'
        )

    creds = None
    with open(file_path, 'r') as json_file:
        creds = json.load(json_file)

    sf = simple_salesforce.Salesforce(
        username=creds["username"],
        password=creds["password"],
        domain=creds["domain"],
        consumer_key=creds["consumer_key"],
        consumer_secret=creds["consumer_secret"]
    )

    return sf