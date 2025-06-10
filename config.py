import os
from os import getenv

API_ID = int(os.environ.get("API_ID", "22272180"))  # Replace "123456" with your actual api_id or use .env
API_HASH = os.environ.get("API_HASH", "c1ca68108649edb2fb0b1e78fe03e780")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

OWNER_ID = int(os.environ.get("OWNER_ID", "5096393058"))  # Your Telegram user ID
SUDO_USERS = list(map(int, os.environ.get("SUDO_USERS", "").split()))  # Space-separated user IDs

MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://kundanvirajbhatt:YA0cwX04q2PSMF8h@cluster0.g5md3iu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")##your mongo url eg: withmongodb+srv://xxxxxxx:xxxxxxx@clusterX.xxxx.mongodb.net/?retryWrites=true&w=majority
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002616654030"))  # Telegram channel ID (with -100 prefix)

PREMIUM_LOGS = os.environ.get("PREMIUM_LOGS", "-1002616654030")  # Optional here you'll get all logs
