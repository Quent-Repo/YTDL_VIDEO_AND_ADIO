import urllib
import re
import ssl
import os
from pytube import YouTube

done = False

#Holder
def converter(r):
    Hold = ""
    return (Hold.join(r))

out = []
while not done:
    link = input("Link (leave blank to quit)? ")
    ending = input("mp4 or mp3? ")
    if link == "":
        print("\n\n\n")
        print("Youtube Downloader V7 By Yudosai  \n\nwith great help from the pytube library")
        print("\n\nThanks for your support <3")
        break
    # link = "https://youtu.be/rQIwHD_ITIo"

    ssl._create_default_https_context = ssl._create_unverified_context
    x = YouTube(link)  # .str
    title = str(x.title)
    s = x.streaming_data
    title = re.sub('[^A-Za-z0-9?.`!@#$%^&*| ]+', '', title)
    print("\n\nTITLE:  " + title)

    ##My eddit
    Title_CMD = []
    for x in title:
        if(x == " "):
            Title_CMD.append("\ ")
        else:
            Title_CMD.append(x)
    #Debug#
    print(converter(Title_CMD))
    ######
    DONE = converter(Title_CMD)

    # print(s["formats"][2]["url"])

    video = urllib.request.urlopen(s["formats"][len(s["formats"]) - 1]["url"])
    print("Video Located... downloading")
    with open(title + '.mp4', 'wb') as output:
        while True:
            chunk = video.read(16 * 1024)
            if not chunk:
                break
            output.write(chunk)
    output.close()

    ## Command Line convert to mp3 can be replaced with anyother kind of format
    print("\n\n" + title)
    if(ending == "mp3"):
        os.system("ffmpeg -i " + DONE + ".mp4 " + DONE + ".gif")
        print("\n\n" + title)
        print("done")
    else:
    	print("done")

##TODO https://www.youtube.com/watch?v=e9o5dEGGHcA