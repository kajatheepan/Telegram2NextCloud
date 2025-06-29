class Translation(object):
    """
    Contains all user-facing messages and responses for the TG2DMS Bot.
    """
    WELCOME = (
        "**Hello {username}!** 👋\n\n"
        "I'm your TG2DMS Bot, ready to help you upload files from Telegram to NextCloud 📤\n\n"
        "Your NextCloud server: **{nextcloud_url}**\n"
        "To get started, please log in to your NextCloud account.\n\n"
        "Type `/help` to see all available commands!"
    )

    START = (
        "**Bot is up and running!**\n\n"
        "Type `/help` to explore what I can do! 💡"
    )

    HELP = (
        "**Here's how you can use me:**\n\n"
        "🔹 `/start` – Start the bot\n"
        "🔹 `/help` – Show this help message\n"
        "🔹 `/login username password` – Log in to your WebDAV account\n"
        "🔹 `/upload` – Upload a Telegram file to your NextCloud\n"
        "🔹 `/batch` – Upload multiple files at once\n\n"
        "_Note: Make sure you're logged in before using upload or batch features._"
    )

    ERROR = (
        "**Oops! Something went wrong.**\n"
        "Please try again later."
    )

    DOWNLOAD_SUCCESS = ("**File downloaded successfully!** 🎉"
                        "\n\n"
                        "Now Uploading to Your NextCloud...")

    DOWNLOAD_FAILURE = (
        "**Download failed!**\n"
        "Please check the file path and try again."
    )

    FILE_NOT_FOUND = (
        "**File not found!**\n"
        "Please double-check the file name or path."
    )

    INVALID_COMMAND = (
        "**Invalid command!**\n"
        "Type `/help` to see the available options."
    )

    INVALID_LOGIN_CMD = "**Invalid Login Command**\n\nUsage: `/login username password`"

    LOGIN_SUCCESS = (
        "**Login successful!**\n"
        "You're all set to use the bot. 🔓"
        "\n\n"
        "**🗑️ Used Quota:** `{used_quota}`\n" \
        "**📦 Total Quota:** `{total_quota}`\n"
    )

    LOGIN_ALREADY = (
        "You're already logged in! No need for a double-dip. 😄"
    )

    LOGIN_REQUIRED = ("**You need to login to continue.**"
                      "\n\nUse `/login username password` to log in to your NextCloud account.")

    UPLOAD_SUCCESS = (
        "**Upload complete!**\n\n"
        "**📄 File:** `{file_name}`\n"
        "**📦 Size:** `{size}`"
    )

    UPLOAD_FAILURE = (
        "**Upload failed!**\n"
        "Please check your login and try again."
    )

    INSUFFICIENT_QUOTA = (
        "**Not enough space to upload this file!**\n\n"
        "🗑️ Maybe delete a few files and try again 😅"
    )
