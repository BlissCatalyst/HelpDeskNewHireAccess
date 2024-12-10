import os
import sys
from dotenv import load_dotenv
from config.user import get_ADUser
from BeyondTrust.auth.BTauth import BT_get_token
from BeyondTrust.newUser.user import create_user

# Load environment variables
load_dotenv()

# Load command line arguments
cmd_arg = sys.argv[1]

# Load the new hire that needs access to Help Desk programs including their name and email. Username is also attached.
new_hire = get_ADUser(cmd_arg)

# BTaccess_token = BT_get_token()["access_token"]

# create_user(BTaccess_token, "HelpDesk Test", "HelpDeskTest@ensignservices.net")
# create_user(BTaccess_token, new_hire.name, new_hire.email)
