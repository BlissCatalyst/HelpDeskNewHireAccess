import os
from dotenv import load_dotenv
from google.oauth2 import service_account

load_dotenv()
GOOGLE_SVC_AUTHORIZE = os.getenv("GOOGLE_SVC_AUTHORIZE")


def create_google_credentials():
    SCOPES = ['https://www.googleapis.com/auth/admin.directory.user', 'https://www.googleapis.com/auth/admin.directory.rolemanagement']
    SERVICE_ACCOUNT_FILE = os.path.abspath('./GoogleAdmin/auth/hd-new-hire-access-3e448db21170.json')

    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES, subject=GOOGLE_SVC_AUTHORIZE)

    return credentials
