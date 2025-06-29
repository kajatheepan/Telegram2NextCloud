from pyrogram import Client as bot
from pyrogram import filters, enums
from pyrogram.types import Message
from translation import Translation
from helper.humanbytes import humanbytes
from helper.logger import logging

logger = logging.getLogger(__name__)

@bot.on_message(filters.command(['upload']))
async def download_command(client, message):
    nextcloud_client = client.user_sessions.get(message.from_user.id, None)

    # Check if the user is logged in
    if nextcloud_client == None or nextcloud_client.islogged_in == False:
        await message.reply_text(Translation.LOGIN_REQUIRED, parse_mode=enums.ParseMode.MARKDOWN)
        return

    if message.reply_to_message:
        reply_message = message.reply_to_message
    
        if reply_message.document or reply_message.video or reply_message.audio or reply_message.photo:
            file_name = reply_message.document.file_name if reply_message.document else \
                        reply_message.video.file_name if reply_message.video else \
                        reply_message.audio.file_name if reply_message.audio else \
                        f"photo_{reply_message.photo.file_id}.jpg"
            file_size = reply_message.document.file_size if reply_message.document else \
                        reply_message.video.file_size if reply_message.video else \
                        reply_message.audio.file_size if reply_message.audio else \
                        reply_message.photo.file_size
            
            file_path = f"./downloads/{file_name}"
            logger.info(f"Preparing to download file: {file_name} ({humanbytes(file_size)})")

            #check for sufficient quota
            if file_size > nextcloud_client.available_quota:
                logger.warning(f"Insufficient quota for user {message.from_user.id}. Required: {humanbytes(file_size)}")
                await message.reply_text(Translation.DOWNLOAD_FAILURE + "\n" + Translation.INSUFFICIENT_QUOTA, parse_mode=enums.ParseMode.MARKDOWN)
                return
            
            try:
                logger.info(f"Starting download of file: {file_name}")
                await client.download_media(reply_message, file_path)
                await message.reply_text(Translation.DOWNLOAD_SUCCESS, parse_mode=enums.ParseMode.MARKDOWN)
                
                # Upload to NextCloud Server
                upload_response = await nextcloud_client.upload(file_path, file_name)
                if upload_response==True:
                    await message.reply_text(Translation.UPLOAD_SUCCESS.format(file_name=file_name, size=humanbytes(file_size)), parse_mode=enums.ParseMode.MARKDOWN)
            except Exception as e:
                logger.error(f"Error during download/upload process: {str(e)}", exc_info=True)
                await message.reply_text(f"{Translation.DOWNLOAD_FAILURE}\nError: {str(e)}")
                
    else:
        logger.warning(f"User {message.from_user.id} did not reply to a media message")
        await message.reply_text("Please reply to a media message to download it.", parse_mode=enums.ParseMode.MARKDOWN)
