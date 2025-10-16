# Copyright (C) @TheSmartBisnu
# Channel: https://t.me/itsSmartDev

import re

API_ID = "29568441" # Your Telegram API ID
API_HASH = "b32ec0fb66d22da6f77d355fbace4f2a" # Your Telegram API Hash
BOT_TOKEN = "8390890269:AAEtQ0KLx-ciASM3ahNYcu1gXuNUZmb2JQ8" # Your Bot Token

# MongoDB connection URI
MONGO_URI = "mongodb+srv://SHINUBHAI:SHINUBHAI@shinubhai.juazqyo.mongodb.net/?retryWrites=true&w=majority&appName=SHINUBHAI"

DEFAULT_WARNING_LIMIT = 3
DEFAULT_PUNISHMENT = "mute" # Options: "mute", "ban"
DEFAULT_CONFIG = ("warn", DEFAULT_WARNING_LIMIT, DEFAULT_PUNISHMENT)

# Regex pattern to detect URLs in user bios
URL_PATTERN = re.compile(
    r'(https?://|www\.)[a-zA-Z0-9.\-]+(\.[a-zA-Z]{2,})+(/[a-zA-Z0-9._%+-]*)*' #done change here
)
