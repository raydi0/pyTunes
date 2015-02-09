''' This is Noah and Rahim's final project. This program will search the user's
file for music using the sys input, display it nicely, and then will play it.
This music player will be called Konsole.

This program uses the Mutagen import for python to both identify which type of
music file the file is and subsequently gather necessary data from it
'''
#from __future__ import print_function
import sys
import os
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3

# Citations:
# http://stackoverflow.com/questions/8948/accessing-mp3-meta-data-with-python
# http://stackoverflow.com/questions/3964681/find-all-files-in-directory-with-extension-txt-with-python

# Defines an empty list of song filepaths to be appended, as well as a dictionary
# which will contain all the song information
global song_dictionary
song_dictionary = {}
global library
library = []
global query
# Sets the query of the search
query = raw_input("Please enter your query: ")


def search_all(dictionary, query):
    '''Defines a function to search through all the attributes of a song to match the query'''
    return_list = []    
    for x in dictionary:
        for y in dictionary[x]:
            if query in y:
                return_list.append(dictionary[x])
    return return_list

def search_artists(dictionary, query):
    '''Defines a function to search through all artists to find a match with the query'''
    return_list = []
    for x in dictionary:
        if query.upper() in dictionary[x][0].upper():
            if dictionary[x][0] not in return_list:
                return_list.append(dictionary[x][0])
    return return_list

def search_songs(dictionary, query):
    '''Defines a function to search through all songs to find a match with the query'''
    return_list = []
    for x in dictionary:
        if query.upper() in dictionary[x][2].upper():
            return_list.append(dictionary[x][2])
    return return_list

def search_albums(dictionary, query):
    '''Defines a function to search through all albums to find a match with the query'''
    return_list = []
    for x in dictionary:
        if query.upper() in dictionary[x][1].upper():
            return_list.append(dictionary[x][1])
    return return_list

def show_albums(artist_choice):
    '''Defines a function to return all the albums of a given artist'''
    return_list=[]
    for x in song_dictionary:
        if artist_choice in song_dictionary[x][0]:
            if song_dictionary[x][1] not in return_list:
                return_list.append(song_dictionary[x][1])
    return return_list

def show_songs(artist_choice, album_choice):
    '''Defines a function to return all the albums of a given artist'''
    return_list=[]
    for x in song_dictionary:
        if album_choice in song_dictionary[x][1] and artist_choice in song_dictionary[x][0]:
            return_list.append(song_dictionary[x][2])
    return return_list
        
# Code to add all song filepaths to a library list
def create_lib(dir_path):
    
    global library
    
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file.endswith((".mp3", ".flac")):
                file_path = str(root) + "/" + str(file)
                library.append(file_path)
    return library

# Code that reads all songs in the library list and adds to the song_dictionary all the
# song information
def read_data(library):
    
    global song_dictionary

    for songs in library:
        song = MP3(songs, ID3=EasyID3)
        song_data = str(song).split(',')
        song_file = ['','','','','']
        for data in song_data:
            end = len(data)
            entry = -1
            if 'artist' in data:
                entry = 0
            if 'album' in data:
                entry = 1
            if 'title' in data:
                entry = 2
            if 'genre' in data:
                entry = 3
            if 'tracknumber' in data:
                entry = 4
            for a in range (0, len(data)-1):
                if "[u'" in data[a:a+3]:
                    start = a+3
                if "']" in data[a:a+2]:
                    end = a
            real_data = data[start:end]
            if entry == 0:
                song_file[0] = real_data
            elif entry == 1:
                song_file[1] = real_data
            elif entry == 2:
                song_file[2] = real_data
            elif entry == 3:
                song_file[3] = real_data
            elif entry == 4:
                song_file[4] = real_data
            elif entry == -1:
                pass
        song_dictionary[songs] = song_file
    return song_dictionary


if __name__ == '__main__':

# Sets the directory path where the music is located
    currentDir = os.getcwd()
    lib_dir = "%s/Music_Library"%currentDir
    
    mainDict = read_data(create_lib(lib_dir))
    

'''
We need:
Ignore lowercase and uppercase
Input for query
Code to display all albums when an artists is searched for
Ability to choose which type of search to do
Ability to play the song
GUI to display things nicely
Add a function to organize a loose mp3 file into correct root
'''

# Input arguements for gathering choices - looks through entire home (or music)
# directory for any .mp3, .wav, etc. files and gathers information from the actual
# file like artist, probably using unpack.
#if query in artist_list:
# Display of all matches for the query
# Code to let the user choose what to play
# Play music
