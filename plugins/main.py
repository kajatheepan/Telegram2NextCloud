from pyrogram import Client as bot
from pyrogram.types import Message  
from pyrogram import filters, enums
from translation import Translation
import re
from webdav3.client import Client as WebDAVClient
from xml.etree import ElementTree
from helper.nextcloud import nextcloud 



@bot.on_message(filters.command(['start']))
async def start_command(client: bot, message: Message):
    url = nextcloud.upload_point
    match = re.match(r"(https?://[^/]+/)", url)
    if match:
        base_url = match.group(1)

    await message.reply_text(Translation.WELCOME.format(username=message.from_user.first_name, nextcloud_url=base_url), parse_mode=enums.ParseMode.MARKDOWN)


@bot.on_message(filters.command(['help']))
async def help_command(client: bot, message: Message):

    await message.reply_text(Translation.HELP, parse_mode=enums.ParseMode.MARKDOWN)

