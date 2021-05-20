# helper-bot
05/19/2021


Use Discord Slash Commands to offer people helpful advice

To add your bot to your discord server with the appropriate permissions, ensure that the permission for `applications.commands` exists in addition to the `bot` OAUTH scope. Without this you will receive 

    "403 Forbidden (error code: 50001): Missing Access"

### Set-Up
In order to run this bot you need `Python >= 3.6` and the required dependencies installed.
You can do this by executing `pip install -r requirements.txt`

### Environmental Variables:

Following enviromental variables are required in order to run the bot:
* `SERVER_ID`
Discord Guild/Server ID | This also acts as the "everyone" role ID
* `LUMENAUT_ROLE_ID`
Role ID that should have permissions to use special commands
* `BOT_TOKEN`
Discord Bot Token 

### Usage:

After you set everything up you are able to run this application using

    python bot.py


### Note:
Any links between channels specified in messages will still crosslink between servers for ease of use. 
E.g. `Please try the fixes and suggestions provided in our <#765222197518139404> channel` will create a link to the Stellar FAQ channel, even if posted in another server. 
