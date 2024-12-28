import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
que = {}
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("7041835456:AAGs-YwuA78Z6U_H_1gscDKUjjvSs_Xm9hw")
BOT_NAME = getenv("BOT_NAME", "ᴄʏʙᴇʀ ᴍᴜsɪᴄ ʙᴏᴛ")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/6790864f5fe27471bdc8d.png")
THUMB_IMG = getenv("THUMB_IMG", "https://telegra.ph/file/e9a4d6655e5ddf51f9160.jpg")
AUD_IMG = getenv("AUD_IMG", "https://telegra.ph/file/91034f175d41040d45b38.jpg")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/c8a0e9c544c5ea689caf9.jpg")
API_ID = int(getenv("12089203"))
API_HASH = getenv("7d85eb5ce156d35f22500fd8ef43e7c2")
BOT_USERNAME = getenv("BOT_USERNAME", "CyberMusikBot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "SaitamaHelper")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "CyberSupportGroup")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "CyberMusicProject")
OWNER_NAME = getenv("OWNER_NAME", "Badboyanim") # isi dengan username kamu tanpa simbol @
PMPERMIT = getenv("PMPERMIT", None)
OWNER_ID = int(os.environ.get("1459770505")) # fill with your id as the owner of the bot
DATABASE_URL = os.environ.get("BQC4d3MALg1Hs9N-Z0vTrL5SWmflG-SHq4xTs_xiT_gvw-yxZLDFKejPb0pQVL3gk_5FdUTa4GCcPEP-idojJinq40IcHSkJ1wMbf81cjQQyJjexFbeeDAT-rcBkeWGh8WKUIJUVhLjJxmnkOy_s1C9KU60IfyBcWE7wWefz8KmyUm7xfrsayq5zURvT-0m65vfbCln-mO3MQu6cti4w_ax6OaIFnsOMizTzhTCyJS0jzCD84_yS1leljyYP_Z7vMrK86oda0EDcXAkq6lULjrWH9xWo7um47eHnAS9-5NyG6wyCj_Veb14IAiITnF_u-DLqCT-iDCApLlJdlgl6cnJyyZmnOgAAAAHLsxF2AA") # fill with your mongodb url
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL")) # make a private channel and get the channel id
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False)) # just fill with True or False (optional)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
LANG = getenv("LANG", "id")
