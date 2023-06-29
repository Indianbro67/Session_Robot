import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("API_ID", "26670684").strip()
API_HASH = os.getenv("API_HASH", "60592bded0f25a9633a8133601f2c779").strip()
BOT_TOKEN = os.getenv("BOT_TOKEN", "6157850456:AAECSQKBOrjcmF_mI9ngnltvsHqjV7TBOEk").strip()
MUST_JOIN = os.getenv("MUST_JOIN", "@test94509")

if not API_ID:
    print("No API_ID found. Exiting...")
    raise SystemExit
if not API_HASH:
    print("No API_HASH found. Exiting...")
    raise SystemExit
if not BOT_TOKEN:
    print("No BOT_TOKEN found. Exiting...")
    raise SystemExit
if not DATABASE_URL:
    print("No DATABASE_URL found. Exiting...")
    raise SystemExit

try:
    API_ID = int(API_ID)
except ValueError:
    print("API_ID is not a valid integer. Exiting...")
    raise SystemExit

if "postgres" in DATABASE_URL and "postgresql" not in DATABASE_URL:
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
