import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = 31343770
API_HASH = "2ed4a8bfcd6e4a3bc650278a162b625e"
BOT_TOKEN = "6399140480:AAFeCQxpOxBfa4sUr9ji3XEGQEJtXNKRCiw"

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))
PICS = (environ.get(
    'PICS',
    'https://telegra.ph/file/b0d44589e96a84ae3123b.jpg https://telegra.ph/file/b0d44589e96a84ae3123b.jpg'
)).split()

# Admins, Channels & Users
ADMINS = [5124873527]
CHANNELS = [1811444060]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_URI = "mongodb+srv://dheerajsharma23949_db_user:P3kaHF7FnOaSt10@accepttheself.ygag34g.mongodb.net/?appName=Accepttheself"
DATABASE_NAME = "dheerajsharma23949_db_user"
COLLECTION_NAME = "Telegram_files"

# Others
LOG_CHANNEL = 3494470609
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'TeamEvamaria')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)
IMDB = is_enabled((environ.get('IMDB', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "False")), False)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", None)
IMDB_TEMPLATE = environ.get(
    "IMDB_TEMPLATE",
    "<b>Query: {query}</b> \n‌IMDb Data:\n\n🏷 Title: <a href={url}>{title}</a>\n🎭 Genres: {genres}\n📆 Year: <a href={url}/releaseinfo>{year}</a>\n🌟 Rating: <a href={url}/ratings>{rating}</a> / 10"
)
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = LOG_CHANNEL
