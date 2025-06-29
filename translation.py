class Translation(object):
    WELCOME = "👋 Welcome! I'm TG2DMS bot. Let's get started.\n\n I can help you to upload your Telegram files to your NextCloud Server"
    START = "🚀 Bot is up and running. Type /help to explore what I can do!"
    
    HELP = (
        "📚 **Here's how you can use me:**\n\n"
        "`/start` – Start the bot\n"
        "`/help` – Show this help message\n"
        "`/login <username> <password>` – Log in to your WebDAV account\n"
        "`/upload' – Upload a Telegram file to  Your NextCloud\n"
        "`/batch` – Upload multiple files at once\n\n"
        "ℹ️ Make sure you're logged in before using upload or download features."
    )
    
    ERROR = "😕 Oops! Something went wrong. Please try again later."
    DOWNLOAD_SUCCESS = "✅ File downloaded successfully!"
    DOWNLOAD_FAILURE = "❌ Couldn't download the file. Check the file path and try again."
    FILE_NOT_FOUND = "🔍 File not found. Please double-check the name or path."
    INVALID_COMMAND = "⚠️ Invalid command. Type `/help` to see what you can do."
    
    INVALID_LOGIN_CMD = (
        "🔐 Invalid login format.\n"
        "Please use:\n"
        "`/login <username> <password>`"
    )
    
    LOGIN_SUCCESS = "🎉 Login successful! You're all set to use the bot."
    LOGIN_ALREADY = "👀 You’re already logged in. No need to do it again."
    LOGIN_REQUIRED = (
        "🔐 You need to log in first to use this feature.\n"
        "Use: `/login <username> <password>`"
    )
    
    UPLOAD_SUCCESS = (
        "✅ Upload complete!\n"
        "**File:** `{file_name}`\n"
        "**Size:** `{size}`"
    )
    
    UPLOAD_FAILURE = "❌ Upload failed. Please check your login and try again."
    
    INSUFFICIENT_QUOTA = (
        "📦 Not enough space to upload this file.\n"
        "Maybe try deleting a few files and come back 😅"
    )
