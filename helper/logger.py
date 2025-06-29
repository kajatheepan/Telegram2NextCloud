import logging

# Basic logging config for Heroku (stdout)
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s - %(name)s - %(message)s'
)

# Create a logger for importing
logger = logging.getLogger("TelegramBot")
