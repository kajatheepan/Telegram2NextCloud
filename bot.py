from pyrogram import Client, filters
from pyrogram.types import Message
from config import Configs as Config
from helper.logger import logging


bot_token = Config.BOT_TOKEN  # Replace with your actual Bot Token
workers = Config.WORKERS  # Number of workers for handling requests
plugins = dict(root="plugins")  # Directory where your plugins are located

app = Client("TGbot", bot_token= bot_token,
             plugins=plugins,
             workers=workers, # Number of workers for handling requests
             max_concurrent_transmissions=Config.MAX_CONCURRENT_TRANSMISSIONS, # Maximum number of concurrent transmissions
             sleep_threshold=60) # Sleep threshold to avoid rate limits


app.user_sessions = {}
app.cooldown_pool = {}  # Set to track users in cooldown
logging.info("Bot is Starting...")
#Run the bot
app.run()



