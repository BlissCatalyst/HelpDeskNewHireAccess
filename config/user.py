import os
from dotenv import load_dotenv
from ldap3 import Server, Connection, ALL

# Load environment variables
load_dotenv()

SERVER_ADDRESS = os.getenv("AD_SERVER_NAME")
USERNAME = os.getenv("USERNAME")
PASSKEY = os.getenv("PASSKEY")


def get_ADUser(AD_username):
    server = Server(SERVER_ADDRESS, get_info=ALL)
    conn = Connection(server, USERNAME, PASSKEY, auto_bind=True)

    search_base = "dc=ensignfs,dc=com"
    search_filter = f"(sAMAccountName={AD_username})"
    search_attributes = ["givenName", "sn", "mail"]

    conn.search(search_base=search_base, search_filter=search_filter,
                attributes=search_attributes)

    # Assuming there is only one result from the search.
    result = conn.entries[0]

    new_hire = userMain(AD_username, result.givenName, result.sn, result.mail)

    return new_hire


class userMain:
    def __init__(self, ADUsername, first_name, last_name, email):
        self.name = f"{first_name} {last_name}"
        self.username = ADUsername
        self.firstName = first_name
        self.lastName = last_name
        self.email = email
