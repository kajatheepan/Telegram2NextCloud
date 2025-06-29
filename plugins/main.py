from pyrogram import Client as bot
from pyrogram.types import Message  
from pyrogram import filters, enums
from translation import Translation
import asyncio
from webdav3.client import Client as WebDAVClient
from xml.etree import ElementTree


@bot.on_message(filters.command(['start']))
async def start_command(client: bot, message: Message):
    await message.reply_text(Translation.WELCOME, parse_mode=enums.ParseMode.MARKDOWN,)
    

@bot.on_message(filters.command(['help']))
async def help_command(client: bot, message: Message):
    await message.reply_text(Translation.HELP,parse_mode=enums.ParseMode.MARKDOWN)

