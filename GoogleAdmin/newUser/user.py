from GoogleAdmin.auth.auth import create_google_credentials
import googleapiclient.discovery
import json

def get_user(newUser):
    credentials = create_google_credentials()

    googleadmin_service = googleapiclient.discovery.build('admin', 'directory_v1', credentials=credentials)

    user_info = googleadmin_service.users().get(userKey=newUser.email).execute()

    print(f"User info: {json.dumps(user_info)}")

    return