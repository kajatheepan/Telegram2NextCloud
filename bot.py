from pyrogram import Client, filters
from pyrogram.types import Message
from config import Configs as Config
from helper.logger import logging
api_id = Config.API_ID  # Replace with your actual API ID=
api_hash = Config.API_HASH # Replace with your actual API Hash
bot_token = Config.BOT_TOKEN  # Replace with your actual Bot Token
plugins = dict(root="plugins")  # Directory where your plugins are located
app = Client("TGbot",api_id= api_id, api_hash=api_hash, bot_token= bot_token,plugins=plugins)


app.user_sessions = {}
logging.info("Bot is Starting...")
#Run the bot
app.run()



