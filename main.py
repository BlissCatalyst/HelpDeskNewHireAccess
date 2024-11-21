from BeyondTrust.auth.BTauth import BT_get_token

# print(BT_get_token())

access_token = BT_get_token()["access_token"]
print(access_token)