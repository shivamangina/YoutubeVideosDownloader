



#  Download youtube videos from a list of urls
#  Usage: python yt.py <file with urls>


from pytube import YouTube
import requests


urls = [
"https://www.youtube.com/watch?v=_DuiIDAYmdU",
"https://www.youtube.com/watch?v=Dai5gSB3XD0",
"https://www.youtube.com/watch?v=CzAFj6mxCjM",
"https://www.youtube.com/watch?v=9KEI84EgLNg",
"https://www.youtube.com/watch?v=HZHzNVw8Fuk",
"https://www.youtube.com/watch?v=MCfMPfkV4FQ",
"https://www.youtube.com/watch?v=3FfyOHMeS-k",
"https://www.youtube.com/watch?v=T1s6Jj7J8V4",
"https://www.youtube.com/watch?v=PrJ1b4zmPcE",
"https://www.youtube.com/watch?v=iRI8UVapFZQ",
"https://www.youtube.com/watch?v=7cPKyE1j07E",
"https://www.youtube.com/watch?v=ABE-6nWuLLU",
"https://www.youtube.com/watch?v=I3Kj7ijPDxk",
"https://www.youtube.com/watch?v=EITgmax_9h8",
"https://www.youtube.com/watch?v=uy4HuVWKGvA",
"https://www.youtube.com/watch?v=WUefjfWp4T0",
"https://www.youtube.com/watch?v=dzRHn98NNaw",
"https://www.youtube.com/watch?v=ZO-vAj3GyUw",
"https://www.youtube.com/watch?v=lqAq4H0vdyo",
"https://www.youtube.com/watch?v=p2f_P2AQLHw",
"https://www.youtube.com/watch?v=xuGd3pgf5dk",
"https://www.youtube.com/watch?v=ojamBqfxVDc",
"https://www.youtube.com/watch?v=zXnftuvENJU",
"https://www.youtube.com/watch?v=9ilsXnwKV3s",
"https://www.youtube.com/watch?v=GVqU15OcLrU",
"https://www.youtube.com/watch?v=NCIEkk3AdWw",
"https://www.youtube.com/watch?v=DOrEJVu2b-w",
"https://www.youtube.com/watch?v=eNxBLCTBmLk",
"https://www.youtube.com/watch?v=4HsVRDDxbHc",
"https://www.youtube.com/watch?v=ip8NSLH15pE",
]

def download_videos(url_list):
    for url in url_list:
        YouTube(url).streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()



def download_thumbnails(url_list):
    for url in url_list:
        yt = YouTube(url)
        thumbnail_url = yt.thumbnail_url

        response = requests.get(thumbnail_url)

        with open(f'{yt.title}.jpg', 'wb') as file:
            file.write(response.content)



download_videos(urls)
download_thumbnails(urls)
