import os
from dotenv import load_dotenv
from BeyondTrust.auth.BTauth import BT_get_token
from BeyondTrust.newUser.user import create_user
from config.user import get_ADUser

# Load environment variables
load_dotenv()

# BTaccess_token = BT_get_token()["access_token"]

# create_user(BTaccess_token, "HelpDesk Test", "HelpDeskTest@ensignservices.net")

get_ADUser(123742866)
