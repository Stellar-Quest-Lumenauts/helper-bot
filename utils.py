import os

# Environmental Variable handling for ease of testing. 
# Anyone can pull the code and put in their own values to test locally instead of modifying static ints in code and accidentally getting checked in

def get_env_vars():
    if os.environ.get("SERVER_ID") is None:
        print("Missing SERVER_ID environment variable, this can be obtained by Server Settings -> Widget -> Server ID")
        exit(1)
    elif os.environ.get("LUMENAUT_ROLE_ID") is None:
        print("Missing LUMENAUT_ROLE_ID environment variable, this can be obtained by Server Settings -> Roles -> Right Click Desired Role -> Copy ID")
        exit(1)
    elif os.environ.get("BOT_TOKEN") is None:
        print("Missing BOT_TOKEN environment variable")
        exit(1)
    try: 
        server_id = int(os.environ.get("SERVER_ID"))
        role_id = int(os.environ.get("LUMENAUT_ROLE_ID"))
        bot_token = os.environ.get("BOT_TOKEN")
        return server_id, role_id, bot_token
    except ValueError as e:
        print("Please verify that both SERVER_ID and LUMENAUT_ROLE_ID are integers")
        print("Exception Details: " + str(e))
        exit(1)