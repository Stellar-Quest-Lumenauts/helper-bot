# helper-bot
05/19/2021


Use Discord Slash Commands to offer people helpful advice

To add your bot to your discord server with the appropriate permissions, ensure that the permission for applications.commands exists in addition to the bot OAUTH scope. Without this you will receive 

    "403 Forbidden (error code: 50001): Missing Access"


Dependencies: 

    pip install discord.py
    pip install git+https://github.com/eunwoo1104/discord-py-slash-command.git 
    *discord-py-slash-command requires the latest release from git as the bot uses features that aren't available on the Python Package Index release*



To run: 

    Set Environmental Variables:
        SERVER_ID = Discord Guild/Server ID | This also acts as the "everyone" role ID
        LUMENAUT_ROLE_ID = Role ID that should have permissions to use special commands
        BOT_TOKEN = Discord Bot Token 
    
    Ensure Dependencies listed above are installed

    python bot.py



Note:
    Any links between channels specified in messages will still crosslink between servers for ease of use. 
    E.g. Please try the fixes and suggestions provided in our <#765222197518139404> channel. Will create a link to the Stellar FAQ channel, even if posted in another server. 
