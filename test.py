#!/usr/bin/env python

# Citation: http://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter

import Tkinter as tk

TITLE_FONT = ("Helvetica", 18, "bold")
class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (QueryFrame, ArtistFrame, AlbumFrame, SongFrame):
            frame = F(container, self)
            self.frames[F] = frame
            # put all of the pages in the same location; 
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(QueryFrame)

    def show_frame(self, c):
        '''Show a frame for the given class'''
        frame = self.frames[c]
        frame.tkraise()

class QueryFrame(tk.Frame):
    def __init__(self, parent, controller):
        
        global query
        tk.Frame.__init__(self, parent) 
        label = tk.Label(self, text="pyTunes Music Library", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        search = tk.Label(self, text="Enter Query: ")
        search.pack(side="top")
        query = Entry(tk.Frame)
        query.pack(side="bottom")
        
        button1 = tk.Button(self, text="Search by Artist", 
                            command=lambda: controller.show_frame(ArtistFrame))
        button2 = tk.Button(self, text="Search by Album",
                            command=lambda: controller.show_frame(AlbumFrame))
        button3 = tk.Button(self, text="Search by Songs",
                    command=lambda: controller.show_frame(SongFrame))
        button1.pack()
        button2.pack()
        button3.pack()


class ArtistFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent) 
        label = tk.Label(self, text="This is page 1", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page", 
                           command=lambda: controller.show_frame(QueryFrame))
        button.pack()

class AlbumFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="This is page 2", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page", 
                           command=lambda: controller.show_frame(QueryFrame))
        button.pack()
        
class SongFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="This is page 2", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page", 
                           command=lambda: controller.show_frame(QueryFrame))
        button.pack()

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()