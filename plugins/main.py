from pyrogram import Client as bot
from pyrogram.types import Message  
from pyrogram import filters, enums
from translation import Translation
import re
from xml.etree import ElementTree
from helper.nextcloud import nextcloud 
from helper.logger import logger


@bot.on_message(filters.command(['start']))
async def start_command(client: bot, message: Message):
    try:
        url = nextcloud.upload_point
        match = re.match(r"(https?://[^/]+/)", url)
        if match:
            base_url = match.group(1)
        
        logger.info(f"Start command received from user {message.from_user.first_name} (ID: {message.from_user.id})")
        await message.reply_text(Translation.WELCOME.format(username=message.from_user.first_name, nextcloud_url=base_url), parse_mode=enums.ParseMode.MARKDOWN)
    except Exception as e:
        logger.error(f"Error in start_command: {str(e)}")
        await message.reply_text("An error occurred while processing your request.")

@bot.on_message(filters.command(['help']))
async def help_command(client: bot, message: Message):
    try:
        await message.reply_text(Translation.HELP, parse_mode=enums.ParseMode.MARKDOWN)
    except Exception as e:
        logger.error(f"Error in help_command: {str(e)}")
        await message.reply_text("An error occurred while processing your request.")
