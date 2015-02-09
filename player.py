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


def calculate(*args):
    try:
        value = float(feet.get())
        meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass
    
root = Tk()
root.title("Feet to Meters")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

feet = StringVar()
meters = StringVar()

feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind('<Return>', calculate)

root.mainloop