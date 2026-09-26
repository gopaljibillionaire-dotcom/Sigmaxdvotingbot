# config.py

BOT_TOKEN = "8983484049:AAGstgl80-20c6pF0Pvgiz2FLA2YWpMQ3pM"
API_ID = 34271171
API_HASH = "434d1585320580b4070a2c7d6b2fafcd"
OWNER_ID = [7952327997, 7636332528, 7489988262] 

# MongoDB Configuration
MONGO_URI =  "mongodb+srv://gopaljichoubey12:gopaljichoubey12@cluster0.qslas8u.mongodb.net/?appName=Cluster0"
DB_NAME = "automation_bot"

# ========== PREMIUM CUSTOM EMOJI IDs ==========
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

# Expanded positive reaction emojis for multi-select
NORMAL_EMOJIS = [
    "🔥", "❤️", "👍", "😍", "🎉", "💯", "👏", "🥳", "😁", "🤩",
    "😎", "🙌", "💪", "✨", "🌟", "💖", "💘", "💝", "💕", "💞",
    "💓", "💗", "💯", "🎊", "🎈", "🎁", "🏆", "🥇", "🥈", "🥉",
    "🎯", "🚀", "⭐", "🌈", "☀️", "🍀", "🌹", "🌸", "💐", "🎵"
]

AVAILABLE_REACTIONS = NORMAL_EMOJIS + ["😱", "🤬", "😢", "💩", "🙏"]

DEFAULT_DELAY = 0.5
