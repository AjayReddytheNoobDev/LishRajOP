from os import path

from yt_dlp import YoutubeDL

from config import DURATION_LIMIT
from helpers.errors import DurationLimitError

ydl_opts = {
    "format": "bestaudio[ext=m4a]",
    "geo-bypass": True,
    "nocheckcertificate": True,
    "outtmpl": "downloads/%(id)s.%(ext)s",
}
ydl = YoutubeDL(ydl_opts)


def download(url: str) -> str:
    info = ydl.extract_info(url, False)
    duration = round(info["duration"] / 60)
    if duration > DURATION_LIMIT:
        raise DurationLimitError(
            f"Abe oo,, Itna lamba video Videos longer than {DURATION_LIMIT} minute(s) not allowed, this video is {duration} minute(s)"
        )
    ydl.download([url])
    return path.join("downloads", f"{info['id']}.{info['ext']}")
