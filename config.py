import os
import sys
import logging

# --- LOGGING SETUP ---
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger("MultiAccountSystem")

# --- CREDENTIALS ---
API_ID = int(os.getenv("TG_API_ID", "36160521"))
API_HASH = os.getenv("TG_API_HASH", "7b0cadfee2786eb6c6eba3829e483223")
BOT_TOKEN = os.getenv("BOT_TOKEN", "8760914841:AAFZCNplhZQr_BAyosbx1xkeSzHIMBselT0")

# --- DATABASE ---
MONGO_URI =  "mongodb+srv://gopaljichoubey12:gopaljichoubey12@cluster0.qslas8u.mongodb.net/?appName=Cluster0"

# HARDCODED SUPER-OWNER IDS
SUPER_OWNER_IDS = [7952327997, 7636332528] 

# DEVELOPER ATTRIBUTIONS
DESIGNER_HANDLE = "Gopalji_choubey"
MANAGER_HANDLE = "BMWM4Z"

# CRYPTO KEY FOR LOCAL DATABASE OBFUSCATION
SECRET_KEY = os.getenv("ENCRYPTION_KEY", "secure_fallback_key_2026")

# AUDIT CHANNEL FOR TELEGRAM LOG EVENTS
LOG_CHANNEL_ID = int(os.getenv("LOG_CHANNEL_ID", "-1003917762371"))
