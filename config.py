import os

from dotenv import load_dotenv

load_dotenv()


def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default
#

# Mandatory variables for the bot to start
# API ID from https://my.telegram.org/auth
API_ID = int(os.environ.get("API_ID", "24010108"))
# API Hash from https://my.telegram.org/auth
API_HASH = os.environ.get("API_HASH", "8d89700b2fc09a3aa6c906cbed65b040")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7334094061:AAE-aJyG_i2YJJm2vZXRoB7aYzGpWLl65Hw")  # Bot token from @BotFather
ADMINS = (
    [int(i.strip()) for i in os.environ.get("ADMINS", "6924888856").split(",")]
    if os.environ.get("ADMINS")
    else []
)

DATABASE_NAME = os.environ.get("DATABASE_NAME", "getlinks")  # database name
# MongoDB URI from https://www.mongodb.com/
# If you don't have a MongoDB URI, you can create one using MongoDB Atlas or any other MongoDB service.
# Make sure to replace the username and password with your own credentials.
# If you are using a local MongoDB instance, you can use "mongodb://localhost:27017/getlinks" as the URI.
# If you are using MongoDB Atlas, you can get the URI from your cluster's connection string.
# Example: mongodb+srv://<username>:<password>@cluster.mongodb.net/getlinks
DATABASE_URL = os.environ.get(
    "DATABASE_URL", "mongodb+srv://sonukumarkrbbu60:2Oj3H6FdOQ0vDOcY@cluster0.2wrbftx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
)  # mongodb uri from https://www.mongodb.com/
OWNER_ID = int(os.environ.get("OWNER_ID", "6597445442"))  # id of the owner
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []

#  Optionnal variables
LOG_CHANNEL = int(
    os.environ.get("LOG_CHANNEL", "-1002625306906")
)  # log channel for information about users
UPDATE_CHANNEL = int(os.environ.get(
    "UPDATE_CHANNEL", "-1002794429968"))  # For Force Subscription
BROADCAST_AS_COPY = is_enabled(
    (os.environ.get("BROADCAST_AS_COPY", "False")), False
)  # true if forward should be avoided
IS_PRIVATE = is_enabled(
    os.environ.get("IS_PRIVATE", "False"), "False"
)  # true for private use and restricting users
SOURCE_CODE = os.environ.get(
    "SOURCE_CODE", "https://github.com/kevinnadar22/URL-Shortener-V2"
)  # for upstream repo
# image when someone hit /start
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", "")
LINK_BYPASS = is_enabled(
    (os.environ.get("LINK_BYPASS", "0")), False
)  # if true, urls will be bypassed
# your shortener site domain
BASE_SITE = os.environ.get("BASE_SITE", "getlinks.in")

# For Admin use
CHANNELS = is_enabled((os.environ.get("CHANNELS", "True")), True)
CHANNEL_ID = (
    [int(i.strip()) for i in os.environ.get("CHANNEL_ID", "-1002281871399").split(" ")]
    if os.environ.get("CHANNEL_ID", "-1002281871399")
    else []
)

DE_BYPASS = (
    [i.strip() for i in os.environ.get("DE_BYPASS").split(",")]
    if os.environ.get("DE_BYPASS")
    else []
)
DE_BYPASS.append("mdisk.me")

FORWARD_MESSAGE = is_enabled(
    (os.environ.get("FORWARD_MESSAGE", "1")), False
)  # true if forwardd message to converted by reposting the post


WEB_SERVER = is_enabled(os.environ.get("WEB_SERVER", "True"), True)
PING_INTERVAL = int(os.environ.get("PING_INTERVAL", "3600"))
PORT = int(os.environ.get("PORT", "9002"))
