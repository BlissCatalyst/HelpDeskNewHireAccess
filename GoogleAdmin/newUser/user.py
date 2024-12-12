import pprint
import json
from GoogleAdmin.auth.auth import create_google_credentials
import googleapiclient.discovery

def get_user(user_id):
    credentials = create_google_credentials()

    googleadmin_service = googleapiclient.discovery.build('admin', 'directory_v1', credentials=credentials)

    user_info = googleadmin_service.users().get(userKey=user_id).execute()

    print(f"User info: {json.dumps(user_info)}")

    return

def get_user_role_assignments(user_id):
    credentials = create_google_credentials()

    googleadmin_service = googleapiclient.discovery.build("admin", "directory_v1", credentials=credentials)

    # user_role_info = googleadmin_service.customer().get()

    return

def get_role_assignment_list(customer_id):
    credentials = create_google_credentials()

    googleadmin_service = googleapiclient.discovery.build("admin", "directory_v1", credentials=credentials)

    role_assignment_list = googleadmin_service.roleAssignments().list(customer=customer_id).execute()

    pprint.pprint(role_assignment_list)

    return