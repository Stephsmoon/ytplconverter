# ================================================== #
# youtube playlist converter v0.0.9
# created by Stephmoon and posted to github
# This takes an url of a youtube playlist and converts the videos
# into audio files which can then be listened to. 
# Quality may vary based on the source on youtube.
# ================================================== #

from pytube import YouTube
from pytube import Playlist

import re
import os
import sys

# ================================================== #
# Create the new directory to store music
# The directory created will be made in the same 
# directory that the file is being runned from. 
# ================================================== #

def create_dir(name, path):
    # Try to Create the Dir; Report Error if not Possible.
    try:
        os.makedirs(path, exist_ok=True)
        print("Directory '%s' created successfully" % name)
    except Exception as error:
        print("Directory '%s' can not be created" % name)
        return error

# ================================================== #
# Converts the Playlist into a Series of mp3 files
# the quality of the mp3 files depends on the quality
# of the video on youtube
# ================================================== #

def convert_playlist(playlist, path):
    for video in playlist.videos:
        # Extract only the Audio
        audio = video.streams.filter(only_audio=True).first()
        # Download the File into new dir
        out_file = audio.download(output_path=path)
        # save the file
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        # result of success
        print(video.title + " has been successfully downloaded.")

# ================================================== #
# Driver Code
# This Driver Code cannot function inside of an Main
# Function since new youtube policy messed with the regex
# or something. 
# ================================================== #

try:
    url = input('Please enter the youtube playlist link:\n>>')
    playlist = Playlist(url)
    name = re.sub("[\";,.!?()*-]\s|[\";,.!?()*-]","", playlist.title)
    path = os.path.join(os.getcwd(), name)
    create_dir(name, path)
    convert_playlist(playlist, path)
    print('Playlist has been Downloaded!')
except Exception as error:
    print(error)
