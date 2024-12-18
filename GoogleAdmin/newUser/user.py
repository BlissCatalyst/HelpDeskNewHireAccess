import os
from dotenv import load_dotenv
import pprint
import json
import googleapiclient.discovery
from GoogleAdmin.auth.auth import create_google_credentials

# Load environment variables
load_dotenv()


def get_user(user_id):
    credentials = create_google_credentials()

    googleadmin_service = googleapiclient.discovery.build(
        'admin', 'directory_v1', credentials=credentials)

    user_info = googleadmin_service.users().get(userKey=user_id).execute()

    print(f"User info: {json.dumps(user_info)}")

    return


def get_role_info_from_id(customer_id, role_id):
    credentials = create_google_credentials()

    googleadmin_service = googleapiclient.discovery.build(
        "admin", "directory_v1", credentials=credentials)

    role_info = googleadmin_service.roles().get(
        customer=customer_id, roleId=role_id).execute()

    print(role_info)

    return


def get_all_roles(customer_id):
    credentials = create_google_credentials()

    googleadmin_service = googleapiclient.discovery.build(
        "admin", "directory_v1", credentials=credentials)

    role_list = googleadmin_service.roles().list(customer=customer_id).execute()

    # pprint.pprint(role_list)
    with open("./GoogleAdmin/newUser/roles.json", "w") as f:
        json.dump(role_list, f)

    return


def get_user_role_assignments(user_id):
    credentials = create_google_credentials()

    googleadmin_service = googleapiclient.discovery.build(
        "admin", "directory_v1", credentials=credentials)

    # user_role_info = googleadmin_service.customer().get()

    return


def get_role_assignment_list(customer_id):
    credentials = create_google_credentials()

    googleadmin_service = googleapiclient.discovery.build(
        "admin", "directory_v1", credentials=credentials)

    role_assignment_list = googleadmin_service.roleAssignments().list(
        customer=customer_id, pageToken="12662052409574184").execute()

    with open("./GoogleAdmin/newUser/role_assignment_list_page2.json", "w") as f:
        json.dump(role_assignment_list, f)

    return


def insert_new_user(newhire_email: str, newhire_first_name: str, newhire_last_name: str, newhire_employeeID: int = None):
    credentials = create_google_credentials()

    googleadmin_service = googleapiclient.discovery.build(
        "admin", "directory_v1", credentials=credentials)

    GOOGLE_TEMP_PASS = os.getenv("GOOGLE_TEMP_PASS")

    body = {
        "primaryEmail": newhire_email,
        "password": GOOGLE_TEMP_PASS,
        "isAdmin": False,
        "suspended": False,
        "changePasswordAtNextLogin": True,
        "ipWhitelisted": False,
        "name": {
            "givenName": newhire_first_name,
            "familyName": newhire_last_name,
            "fullName": f"{newhire_first_name} {newhire_last_name}"
        },
        "emails": [
            {
                "address": newhire_email,
                "primary": True
            },
            {
                "address": f"{newhire_email}.test-google-a.com"
            }
        ],
        "isMailboxSetup": False,
        "includeInGlobalAddressList": True,
        "isEnrolledIn2Sv": False,
        "isEnforcedIn2Sv": False,
        "archived": False,
        "orgUnitPath": "/Google Help Desk Admins only",
        "languages": [
            {
                "languageCode": "en",
                "preference": "preferred"
            }
        ]
        # "externalIds": [
        #     {
        #         "customType": "EID",
        #         "type": "custom",
        #         "value": newhire_employeeID
        #     }
        # ]
    }

    new_user_result = googleadmin_service.users().insert(body=body).execute()

    new_user_role_assign = insert_role_assignment(new_user_result["id"])

    pprint.pprint(new_user_result)

    return


def insert_role_assignment(user_id):
    credentials = create_google_credentials()

    googleadmin_service = googleapiclient.discovery.build(
        "admin", "directory_v1", credentials=credentials)
    
    customer_id = os.getenv("GOOGLE_CUSTOMER_ID")

    # Must assign each role individually
    for role in HD1_roles:
        role["assignedTo"] = user_id
        body = {
            **role,
        }
        new_role_assignment = googleadmin_service.roleAssignments().insert(
            customer=customer_id, body=body).execute()
        pprint.pprint(new_role_assignment)

    return


HD1_roles = [
    {
        "roleId": 12662052409573380,  # Help Desk Administrator
        "assignedTo": None,
        "scopeType": "CUSTOMER",
    },
    {
        "roleId": 12662052409573382,  # EFS-Enrollers
        "assignedTo": None,
        "scopeType": "CUSTOMER",
    },
    {
        "roleId": 12662052409573389,  # Ensign Help Desk
        "assignedTo": None,
        "scopeType": "CUSTOMER",
    }
]
