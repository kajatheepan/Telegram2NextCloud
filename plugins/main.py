from pyrogram import Client as bot
from pyrogram.types import Message  
from pyrogram import filters
from translation import Translation
import asyncio
from webdav3.client import Client as WebDAVClient
from xml.etree import ElementTree


@bot.on_message(filters.command(['start']))
async def start_command(client: bot, message: Message):
    await message.reply_text(Translation.WELCOME)
    

@bot.on_message(filters.command(['help']))
async def help_command(client: bot, message: Message):
    await message.reply_text(Translation.HELP)



# async def upload_file(client: bot, file_path: str, webdav_url: str, username: str, password: str)
"""
Bot Commands:

/start   - Start the bot
/help    - Show help information
/download - Download and upload a file to the DMS server
/batch   - Upload multiple files at once
/login   - Login to the DMS server
/cancel  - Cancel the current operation
/about   - About the bot
"""
