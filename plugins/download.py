from pyrogram import Client as bot
from pyrogram import filters
from pyrogram.types import Message
from translation import Translation
from helper.humanbytes import humanbytes


@bot.on_message(filters.command(['upload']))
async def download_command(client,message):

    nextcloud_client = client.user_sessions.get(message.from_user.id,None)

    # Check if the user is logged in
    if  nextcloud_client == None or nextcloud_client.islogged_in == False:
        await message.reply_text(Translation.LOGIN_REQUIRED)
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

            #check for sufficient quota
            if file_size > nextcloud_client.available_quota:
                await message.reply_text(Translation.DOWNLOAD_FAILURE + "\n" + Translation.INSUFFICIENT_QUOTA)
                return
            
            try:
                await client.download_media(reply_message, file_path)
                await message.reply_text(Translation.DOWNLOAD_SUCCESS)
                # Upload to NextCloud Server
                upload_response = await nextcloud_client.upload(file_path, file_name)
                if upload_response==True:
                    await message.reply_text(Translation.UPLOAD_SUCCESS.format(file_name=file_name, size=humanbytes(file_size)))
            except Exception as e:
                await message.reply_text(f"{Translation.DOWNLOAD_FAILURE}\nError: {str(e)}")
                
    else:
        await message.reply_text("Please reply to a media message to download it.")

    #upload process


# @bot.on_message(filters.command('batch'))
# async def batch_download(client,message):
