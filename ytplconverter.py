# ================================================== #
# youtube playlist converter v0.1.3
# created by Stephmoon and posted to github
# This takes an url of a youtube playlist and converts the videos
# into audio files which can then be listened to. 
# Quality may vary based on the source on youtube.
# ================================================== #

from tqdm import tqdm
from pytube import YouTube
from pytube import Playlist
from moviepy.editor import *

import eyed3
import sys
import re
import os

# ================================================== #
# Create the new directory to store music
# The directory created will be made in the same 
# directory that the file is being runned from. 
# ================================================== #

def create_dir(name, path):
    # Try to Create the Dir; Report Error if not Possible.
    try:
        os.makedirs(path, exist_ok=True)
        print('Directory "%s" created successfully' % name)
    except Exception as error:
        print('Directory "%s" can not be created' % name)
        return error

# ================================================== #
# Converts the Playlist into a Series of mp3 files
# the quality of the mp3 files depends on the quality
# of the video on youtube
# ================================================== #

def convert_playlist(playlist, artist, path):
    for video in tqdm(playlist.videos, desc='downloading playlist...'):
        # Grab the Video from Youtube using Pytube, this will come as an MP4
        yt_video = video.streams.filter().first()
        # Download the File into new dir as an MP4 which will be Converted
        out_audio = yt_video.download(output_path=path)

        print(out_audio)
        # Create the Path for the the MP3 File which will be created
        # The First Forward Slash may need to be changed to Back Slash on Windows Computers
                         # \/
        new_path = path + '/' + re.sub('[\'";,.!?()@$#%&*^-]','',video.title) + '.mp3'
        print(new_path)

        # Convert the MP4 into an MP3 using Moviepy, this makes this a Proper Conversion
        new_audio = VideoFileClip(out_audio)
        new_audio.audio.write_audiofile(new_path,logger=None)
        new_audio.close()
        # Delete the Previous MP4 File now that the MP3 is properly Converted
        os.remove(out_audio)
        # Use eyed3 to Load the File to Change the Metadata
        audio = eyed3.load(new_path)
        # Change the Artist Album and Title of the Song
        audio.tag.artist = artist
        audio.tag.title = video.title
        if artist in playlist.title:
            audio.tag.album = re.sub(artist,'',re.sub(' - ','',playlist.title))
        else:
            audio.tag.album = playlist.title
        # Save the Changes done to the File
        audio.tag.save()
        # result of success
        print('\n' + video.title + ' has been successfully downloaded.')

# ================================================== #
# Driver Code
# This Driver Code cannot function inside of an Main
# Function since new youtube policy messed with the regex
# or something. 
# ================================================== #

user_input = ''
print('\n\n\nyoutube playlist converter v0.1.3.2')
print('Enter your Playlist to Convert the Playlist\nOr enter anything to escape the Program\n')
while user_input.lower() != 'escape':
    url = input('Enter the youtube playlist link (or enter anything to cancel):\n>>')
    playlist = Playlist(url)
    artist = re.sub(' - Topic','', YouTube(url).author) 
    name = re.sub('[\'";,.!?()@$#%&*^-]\s|[\'";,.!?()@$#%&*^-]','',playlist.title)
    path = os.path.join(os.getcwd(), name)
    create_dir(name, path)
    convert_playlist(playlist, artist, path)
    print('Playlist has been Downloaded!')
