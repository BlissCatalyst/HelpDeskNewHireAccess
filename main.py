import os
from dotenv import load_dotenv
from BeyondTrust.auth.BTauth import BT_get_token
from BeyondTrust.newUser.user import create_user
from BeyondTrust.newUser.user import BTNewUser
from BeyondTrust.newUser.user import get_user

# Load environment variables
load_dotenv()

BTaccess_token = BT_get_token()["access_token"]

# create_user(BTaccess_token, "HelpDesk Test", "HelpDeskTest@ensignservices.net")

get_user(698, BTaccess_token)
