import requests
import json
import random
import re
from random import randint
import datetime


def downloadvideo(querystring):
    print('toi 1')
    url = "https://tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com/vid/index"

    # querystrings = {"url":"https://www.tiktok.com/@thaisontran1616/video/7166124273361358107"}
    querystrings = querystring

    headers = {
        "X-RapidAPI-Key": "dd1582884cmsh424c8508c4933b1p1ab7bbjsnfcd1701bcb84",
        "X-RapidAPI-Host": "tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com"
    }
    print('toi 2')

    response = requests.request("GET", url, headers=headers, params=querystrings)
    print('toi 3')

    videos=response.text
    video = videos.replace('[',"")
    # print(video)
    print(str(video))

    link = re.findall(r'{"video":"([^"]+)"',video)
    print(link)
    url_video="".join(link)
    # print(r"url video "+url_video)
    names =random.randrange(1,9000)
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    name = today+"video"+str(names)+".mp4"
    print(r'toi 5'+ name)

    r = requests.get(url_video)
    with open(name, "wb") as f:
        f.write(r.content)


if __name__ == "__main__":
    down= downloadvideo("https://www.tiktok.com/@thaisontran1616/video/7166124273361358107")
