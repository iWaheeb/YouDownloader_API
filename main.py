import httpx

from fastapi import FastAPI

from pytube import YouTube


app = FastAPI()

class YouDownloader_API:

    @app.get("/YouDownloader/vid_size")
    def get_vid_size(yt_link: str):
        try:
            yt = YouTube(yt_link)
            vid_stream = yt.streams.get_highest_resolution()
            size_in_bytes = vid_stream.filesize
            size_in_MB = round(size_in_bytes/1024/1024)
            return f"The video size is {size_in_MB}MB"

        except:
            print("An error occured in the download function")
