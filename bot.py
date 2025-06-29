from pyrogram import Client, filters
from pyrogram.types import Message


api_id = ***REMOVED***  # Replace with your actual API ID=
api_hash = "***REMOVED***"  # Replace with your actual API Hash
bot_token = "***REMOVED***"  # Replace with your actual Bot Token
plugins = dict(root="plugins")  # Directory where your plugins are located
app = Client("TGbot",api_id= api_id, api_hash=api_hash, bot_token= bot_token,plugins=plugins)


app.user_sessions={}
print("Bot is Starting...")
#Run the bot
app.run()



