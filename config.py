# config.py
import os
import logging
from datetime import datetime, timedelta

# Logging Setup
logging.basicConfig(level=logging.ERROR)
logging.getLogger('telethon').setLevel(logging.ERROR)
logging.getLogger('httpx').setLevel(logging.ERROR)

# Bot Configuration (Loaded from Environment Variables)
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
API_ID = int(os.getenv("API_ID", )
API_HASH = os.getenv("API_HASH", "434d1585320580b4070a2c7d6b2fafcd")
MONGO_URI = os.getenv("MONGO_URI", "")

# Owner Configuration
OWNER_IDS = [7952327997, 7636332528, 7489988262]
OWNER_ID = OWNER_IDS[0]  # Default primary owner ID

# Premium Custom Emoji IDs
PREMIUM_EMOJIS = {
    "heart_fire": "5042225965518816316",
    "lightning": "5042334757040423886",
    "location": "5039775669496579510",
    "flower": "6073117703965511893",
    "check": "6147460667281511517",
    "crown": "6235252066554484059",
    "kiss": "6116282026506065674",
    "skull": "6089128873893563936",
    "xmas": "6267071898702583835",
    "monkey": "6273627839862411998",
    "gift": "5893175870096414393",
    "angel": "5893411041030707544",
    "devil": "5893079628469246474",
}

# Normal Positive Reaction Emojis
NORMAL_EMOJIS = [
    "🔥", "❤️", "👍", "😍", "🎉", "💯", "👏", "🥳", "😁", "🤩",
    "😎", "🙌", "💪", "✨", "🌟", "💖", "💘", "💝", "💕", "💞",
    "💓", "💗", "💯", "🎊", "🎈", "🎁", "🏆", "🥇", "🥈", "🥉",
    "🎯", "🚀", "⭐", "🌈", "☀️", "🍀", "🌹", "🌸", "💐", "🎵"
]

AVAILABLE_REACTIONS = NORMAL_EMOJIS + ["😱", "🤬", "😢", "💩", "🙏"]
DEFAULT_DELAY = 0.5

# Helper functions for authorization checks
def is_owner(user_id: int) -> bool:
    return user_id in OWNER_IDS

def styled_button(text, callback_data):
    from telegram import InlineKeyboardButton
    return InlineKeyboardButton(text, callback_data=callback_data)
