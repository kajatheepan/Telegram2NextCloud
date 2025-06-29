
from pyrogram import Client as bot
from pyrogram.types import Message  
from pyrogram import filters
from translation import Translation
from xml.etree import ElementTree
from helper.humanbytes import humanbytes
from helper.checkquota import check_quota
from helper.nextcloud import nextcloud


# @bot.on_message(filters.command(['login']))
# async def login_command(client: bot, message: Message):
#     message_text = message.text.strip().split()
#     if len(message_text) != 4:
        
#         await message.reply_text(Translation.INVALID_LOGIN_CMD)
#     else:
#         webdav_hostname = message_text[1]
#         username = message_text[2]
#         password = message_text[3]
#         #Validate credintials
#         options = {
#             'webdav_hostname': webdav_hostname,
#              'webdav_login': username,
#              'webdav_password': password
#         }
#         try:
#             webdav_client = WebDAVClient(options)
#             free_quota = webdav_client.free()
#             await message.reply_text(f"Connected to {webdav_hostname} as {username} \n Available Quota : {humanbytes(free_quota)} ")
            
            
#             # print("freequota", humanbytes(free_quota))
#             await message.reply_text(Translation.LOGIN_SUCCESS)
#         except Exception as e:
#             print(f"Login failed: {str(e)}")
    

@bot.on_message(filters.command(['login']))
async def login_command(client: bot, message: Message):
    if await check_login(client, message):
        await message.reply_text(Translation.LOGIN_ALREADY)
        return
    message_text = message.text.strip().split()
    if len(message_text) != 3:
        await message.reply_text(Translation.INVALID_LOGIN_CMD)
    else:
        username = message_text[1]
        password = message_text[2]
        try:
            nextcloud_client =  nextcloud(username, password)
            response = await nextcloud_client.login()
            if response:
                client.user_sessions[message.from_user.id] = nextcloud_client
                await message.reply_text(Translation.LOGIN_SUCCESS)
                used_quota = humanbytes(nextcloud_client.used_quota)
                total_quota = humanbytes(nextcloud_client.used_quota+nextcloud_client.available_quota)
                await message.reply_text(f"Used : {used_quota}/{total_quota} ")
        except Exception as e:
            print(f"Login failed: {str(e)}")
            await message.reply_text(f"Login failed: {str(e)}")
            return


async def check_login(client: bot, message: Message):
    if client.user_sessions.get(message.from_user.id) and client.user_sessions[message.from_user.id].islogged_in:
        return True
