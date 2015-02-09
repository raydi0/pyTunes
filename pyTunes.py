''' This is Noah and Rahim's final project. This program will search the user's
file for music using the sys input, display it nicely, and then will play it.
This music player will be called Konsole.

This program uses the Mutagen import for python to both identify which type of
music file the file is and subsequently gather necessary data from it
'''
#from __future__ import print_function
import sys
import os
import glob
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3


# Citations:
# http://stackoverflow.com/questions/8948/accessing-mp3-meta-data-with-python
# http://stackoverflow.com/questions/3964681/find-all-files-in-directory-with-extension-txt-with-python

# Sets the directory path where the music is located
dir_path = "/media/ubuntu/OS/Users/Noah/Music/The Megalomanium/Baths/"

# Sets the query of the search
query = "Smell"

# Defines an empty list of song filepaths to be appended, as well as a dictionary
# which will contain all the song information
library = []
song_dictionary = {}

def search_all(dictionary, query):
    for x in dictionary:
        for y in dictionary[x]:
            if query in y:
                return x
    return None

def search_artists(dictionary, query):
    for x in dictionary:
        if query in dictionary[x][0]:
            return x
    return None

def search_songs(dictionary, query):
    for x in dictionary:
        if query in dictionary[x][2]:
            return x
    return None

def search_albums(dictionary, query):
    for x in dictionary:
        if query in dictionary[x][1]:
            return x
    return None

# Code to add all song filepaths to a library list
for root, dirs, files in os.walk(dir_path):
    for file in files:
        if file.endswith((".mp3", ".flac")):
            file_path = str(root) + "/" + str(file)
            library.append(file_path)

for songs in library:
    song = MP3(songs, ID3=EasyID3)
    song_data = str(song).split(',')
    song_file = ['','','','','']
    for data in song_data:
        if 'artist' in data:
            song_file[0] = data
        if 'album' in data:
            song_file[1] = data
        if 'title' in data:
            song_file[2] = data
        if 'genre' in data:
            song_file[3] = data
        if 'tracknumber' in data:
            song_file[4] = data
    song_dictionary[songs] = song_file

result = search_songs(song_dictionary, query)
print (result)

'''
for file in glob.glob('/media/ubuntu/OS/Users/Noah/Music/The Megalomanium/Baths/*.mp3'):
    print (file)


for file in os.listdir("/media/ubuntu/OS/Users/Noah/Music/The Megalomanium/Alt-J/An Awesome Wave/"):
    if file.endswith(".mp3"):
        print(file)
'''

# Input arguements for gathering choices - looks through entire home (or music)
# directory for any .mp3, .wav, etc. files and gathers information from the actual
# file like artist, probably using unpack.
#if query in artist_list:
# Display of all matches for the query
# Code to let the user choose what to play
# Play music
#