#!/usr/bin/env python

'''
    player.py takes 'DictOfSearchResults' in the form
    {'path/to/song.format': [ 'artist', 'album', 'title', 'genre', 'track number'], ...}
    and displays them in a media player GUI for playback.

        1) init gui ***
        
        2) load songs ***
        
        3) seeking/additional features
            the goal will be to have buttons to display
            search results by artits, album, or genre
        
'''

# cover_grabber
# https://pypi.python.org/pypi/cover_grabber/1.2.1

# tkinter GUI
# Sources:
#   https://www.youtube.com/watch?v=WdmPTH8Qcug
#   http://www.tkdocs.com/tutorial/firstexample.html

import os
from Tkinter import *
import ttk
import pyTunes

global mainDict
mainDict = {}
global artist_list
artist_list = []

currentDir = os.getcwd()
lib_dir = "%s/Music_Library"%currentDir
mainDict = pyTunes.read_data(pyTunes.create_lib(lib_dir))

class Application(Frame):

    def search_artists(self):
        global artist_list
        response = query.get()
        artist_list = pyTunes.search_artists(mainDict, response)
        execfile("artists.py")
        
    def search_songs(self):
        response = query.get()
        print pyTunes.search_songs(mainDict, response)
    
    def search_albums(self):
        response = query.get()
        print pyTunes.search_albums(mainDict, response)
    
    def createWidgets(self):
        global query
        self.query_in = Label(root, text="Enter Query:")
        self.query_in.pack({"side": "top"})

        query = Entry(root)
        query.pack({"side":"bottom"})
        response = query.get()
        
        self.QUIT = Button(self)
        self.QUIT["text"] = "Quit"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit
        self.QUIT.pack({"side": "left"})

        self.by_song = Button(self)
        self.by_song["text"] = "Search by Song Name"
        self.by_song["command"] = self.search_songs
        self.by_song.pack({"side": "left"})
        
        # button to search by artist, album, or song ect
        self.by_artist = Button(self)
        self.by_artist["text"] = "Search by Artist"
        self.by_artist["command"] = self.search_artists
        self.by_artist.pack({"side": "left"})
        
        self.by_album = Button(self)
        self.by_album["text"] = "Search by Album"
        self.by_album["command"] = self.search_albums
        self.by_album.pack({"side": "left"})

    def __init__(self, master=None):    
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()