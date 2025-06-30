# Telegram to NextCloud Bot 🤖

**A simple bot that automatically saves your Telegram media files to your NextCloud instance.
**
## What it does

- Saves photos, videos, documents from Telegram to NextCloud
- Easy to set up and use
- Works in private chats and groups
- Keeps your media organized

## Setup

1. Get your bot token from [@BotFather](https://t.me/BotFather) on Telegram

2. Clone this repository:
```bash
git clone https://github.com/kajatheepan/Telegram2NextCloud.git
cd Telegram-to-NextCloud
```

3. Configure environment variables:
    - Copy `.env.example` to `.env`
    - Edit `.env` with your settings:
      ```
    ```env
    
    BOT_TOKEN="your_telegram_bot_token" # Your Telegram bot token from @BotFather
    
    COOLDOWN_SECONDS="60" # Cooldown between uploads in seconds

    UPLOAD_POINT="https://nextcloud.example.com/remote.php/webdav/" # Your NextCloud WebDAV URL

    WORKERS="3" # Number of worker processes

    MAX_CONCURRENT_TRANSMISSIONS="5" # Maximum concurrent file transfers
    ```
      ```

4. Start the bot:
```bash
python main.py
```

## Usage

1. Login to your NextCloud with `/login` command
2. Send media files to the bot
3. Reply to any media with `/upload` command
4. Bot will save them to your NextCloud



## Need Help?

Open an issue if you run into problems!

## Contributing

Contributions are welcome! Feel free to open issues, submit pull requests, suggest features, or improve documentation.

