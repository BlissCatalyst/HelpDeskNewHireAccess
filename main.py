import os
import sys
from dotenv import load_dotenv

from config.user import get_ADUser

from BeyondTrust.auth.BTauth import BT_get_token
from BeyondTrust.newUser.user import create_user

from GoogleAdmin.newUser.user import get_user, get_role_assignment_list, get_role_info_from_id, get_all_roles, insert_new_user

# Load environment variables
load_dotenv()
# GOOGLE_CUSTOMER_ID = os.getenv("GOOGLE_CUSTOMER_ID")

# Load command line arguments
# cmd_arg = sys.argv[1]

# Load the new hire that needs access to Help Desk programs including their name and email. Username is also attached.
# new_hire = get_ADUser(cmd_arg)

# BTaccess_token = BT_get_token()["access_token"]

# create_user(BTaccess_token, "HelpDesk Test", "HelpDeskTest@ensignservices.net")
# create_user(BTaccess_token, new_hire.name, new_hire.email)

# get_user("")
# get_role_assignment_list(GOOGLE_CUSTOMER_ID)
# get_role_info_from_id(GOOGLE_CUSTOMER_ID, "")
# get_all_roles(GOOGLE_CUSTOMER_ID)

# insert_new_user("HD-newhire-test@ensignservices.net", "HDTestFirst", "HDTestLast")
