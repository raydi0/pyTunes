#!/usr/bin/env python

import os

from Tkinter import *
import ttk
import pyTunes

currentDir = os.getcwd()
lib_dir = "%s/Music_Library"%currentDir
mainDict = pyTunes.read_data(pyTunes.create_lib(lib_dir))

class Application(Frame):
    def show_albums(self):
        pass

    def createWidgets(self):
        artist_list = ["test", "phish", "rhcp"]
        
        for artist in artist_list:
            self.artist = Button(self)
            self.artist["text"] = "%s" %artist
            self.artist["command"] = self.show_albums
            self.artist.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
