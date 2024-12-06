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

    conn.search(search_base=search_base, search_filter=search_filter, attributes=search_attributes)

    for entry in conn.entries:
        print(f"First Name: {entry.givenName}")
        print(f"Last Name: {entry.sn}")
        print(f"Email: {entry.mail}")

    return


class userMain:
    def __init__(self, name, email):
        self.name = name
        self.email = email
