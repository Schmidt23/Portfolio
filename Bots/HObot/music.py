import youtube_dl
import os

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'outtmpl': 'music/%(title)s.mp3',
    'quiet': False
}



def dl_file(url):
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        result = ydl.extract_info(url, download=False)
        outfile = ydl.prepare_filename(result)
    return outfile
