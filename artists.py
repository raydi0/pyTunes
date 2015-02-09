#!/usr/bin/env python

import os

from Tkinter import *
import ttk
import pyTunes

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
