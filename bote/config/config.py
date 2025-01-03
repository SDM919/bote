
import sys
from os import getenv
import os
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()
import re

API_ID = int(getenv("API_ID", "29394559"))
API_HASH = getenv("API_HASH", "9314361e480e6e2d21bbd2c84574499a")
OWNER = int(os.getenv("OWNER", "6800702455"))
BOT_TOKEN = getenv("7529184093:AAEpyFAmsbeyJ0I3Cl7XsyR3vr4zV3X4PgQ")
Muntazer = getenv("Muntazer", "V1PHP")
assistant = getenv("assistant", "Mohmed1_1b")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://omsnkok:muntazer@cluster0.ywxsjao.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "50000"))  
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1002469138148"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "𝐀𝐑𝐀𝐁𝐒")
PROTECT_CONTENT = getenv("PROTECT_CONTENT", "True")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6800702455").split()))
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
UPSTREAM_REPO = getenv("UPSTREAM_REPO","https://github.com/SDM919/bote")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv("GIT_TOKEN","")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/V1PHP")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/helpsdm") 
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", False)
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "50000"))
AUTO_SUGGESTION_TIME = int(getenv("AUTO_SUGGESTION_TIME", "3000"))
AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", False)
PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", "False")
YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "3"))
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "5"))
GITHUB_REPO = getenv("GITHUB_REPO","")
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "19609edb1b9f4ed7be0c8c1342039362")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "409e31d3ddd64af08cfcc3b0f064fcbe")
VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "5"))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "50"))
CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "5")) 
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "2147483648")) 
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "2147483648")) 
SET_CMDS = getenv("SET_CMDS", "False")
STRING1 = getenv("STRING_SESSION", "AgCIVfMAdgFxxB1m_ZmsD1tTF381VSHq8ptTGe_2gn_b_8e2uPHYN30kXH50uSB7nXyjz2ZRIaqFcZkM9jqf5TQ7peLyw49X4g1VBTOwTnzWjRUvJI_TcjTPoBaG3cMN3BzOpJlyQuV-KrhA-XxJvIVZeF0s0FaKsskngwpahGeDS-V4Sgoxi2rgtR77NiTNg1bnFzilKFDNAaLS9yeMGXjPxSUmreRrvcx8tFCHK1RK3iCrN3fBuXfob2PFPoBcrFx1zsYs_CscXLnDAut4_rwVT4Y8IgvulZaFBnnccvccHSIrmYBnMgECRvOcc8hDpreKAq1dmk1OUVu2Ns8BC6Dc2vvxsQAAAAHe2SCyAA")
STRING2 = getenv("STRING_SESSION2", "")
STRING3 = getenv("STRING_SESSION3", "")
STRING4 = getenv("STRING_SESSION4", "")
STRING5 = getenv("STRING_SESSION5", "")
START_IMG_URL = getenv("START_IMG_URL","https://cdn.pixabay.com/photo/2016/02/18/22/17/start-1209831_960_720.jpg")
PING_IMG_URL = getenv("PING_IMG_URL","https://cdn.pixabay.com/photo/2016/06/15/22/50/ping-pong-1465373_960_720.jpg")
PLAYLIST_IMG_URL = getenv("PLAYLIST_IMG_URL","https://cdn.pixabay.com/photo/2017/08/30/07/56/playlist-2696488_960_720.jpg")
GLOBAL_IMG_URL = getenv("GLOBAL_IMG_URL","https://cdn.pixabay.com/photo/2016/03/09/09/23/globe-1249396_960_720.jpg")
STATS_IMG_URL = getenv("STATS_IMG_URL","https://cdn.pixabay.com/photo/2015/05/25/14/13/statistics-783742_960_720.jpg")
TELEGRAM_AUDIO_URL = getenv("TELEGRAM_AUDIO_URL","https://cdn.pixabay.com/photo/2020/07/02/08/26/telegram-5365248_960_720.jpg")
TELEGRAM_VIDEO_URL = getenv("TELEGRAM_VIDEO_URL","https://cdn.pixabay.com/photo/2020/07/02/08/26/telegram-5365248_960_720.jpg")
STREAM_IMG_URL = getenv("STREAM_IMG_URL","https://cdn.pixabay.com/photo/2016/11/18/21/23/stream-1835077_960_720.jpg")
SOUNCLOUD_IMG_URL = getenv("SOUNCLOUD_IMG_URL","https://cdn.pixabay.com/photo/2017/08/05/00/12/soundcloud-2587842_960_720.jpg")
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL","https://cdn.pixabay.com/photo/2013/10/02/23/03/youtube-190559_960_720.jpg")
SPOTIFY_ARTIST_IMG_URL = getenv("SPOTIFY_ARTIST_IMG_URL","https://cdn.pixabay.com/photo/2016/11/19/14/00/spotify-1834162_960_720.jpg")
SPOTIFY_ALBUM_IMG_URL = getenv("SPOTIFY_ALBUM_IMG_URL","https://cdn.pixabay.com/photo/2016/11/19/14/00/spotify-1834162_960_720.jpg")
SPOTIFY_PLAYLIST_IMG_URL = getenv("SPOTIFY_PLAYLIST_IMG_URL","https://cdn.pixabay.com/photo/2016/11/19/14/00/spotify-1834162_960_720.jpg")



def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

if MUSIC_BOT_NAME is None:
    MUSIC_BOT_NAME = "Music player"

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        print(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        print(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()



if STATS_IMG_URL:
    if STATS_IMG_URL != "https://telegra.ph/file/4dd9e2c231eaf7c290404.jpg":
        if not re.match("(?:http|https)://", STATS_IMG_URL):
            print(
                "[ERROR] - Your STATS_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if TELEGRAM_AUDIO_URL:
    if TELEGRAM_AUDIO_URL != "https://telegra.ph/file/8234d704952738ebcda7f.jpg":
        if not re.match("(?:http|https)://", TELEGRAM_AUDIO_URL):
            print(
                "[ERROR] - Your TELEGRAM_AUDIO_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if STREAM_IMG_URL:
    if STREAM_IMG_URL != "https://telegra.ph/file/e24f4a5f695ec5576a8f3.jpg":
        if not re.match("(?:http|https)://", STREAM_IMG_URL):
            print(
                "[ERROR] - Your STREAM_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if SOUNCLOUD_IMG_URL:
    if SOUNCLOUD_IMG_URL != "https://telegra.ph/file/7645d1e04021323c21db9.jpg":
        if not re.match("(?:http|https)://", SOUNCLOUD_IMG_URL):
            print(
                "[ERROR] - Your SOUNCLOUD_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if YOUTUBE_IMG_URL:
    if YOUTUBE_IMG_URL != "https://telegra.ph/file/76d29aa31c40a7f026d7e.jpg":
        if not re.match("(?:http|https)://", YOUTUBE_IMG_URL):
            print(
                "[ERROR] - Your YOUTUBE_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if TELEGRAM_VIDEO_URL:
    if TELEGRAM_VIDEO_URL != "https://telegra.ph/file/8d02ff3bde400e465219a.jpg":
        if not re.match("(?:http|https)://", TELEGRAM_VIDEO_URL):
            print(
                "[ERROR] - Your TELEGRAM_VIDEO_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "Yukkilogs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []
PHOTO = list(
    filter(
        None,
        getenv("PHOTO_LINKS", "").split(),
    )
)
