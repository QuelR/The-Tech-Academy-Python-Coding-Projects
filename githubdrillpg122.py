
import tkinter
from tkinter.filedialog import *
import os
from tkinter import *
import tkinter as tk
import sqlite3

# Frame is the Tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
            
        self.master = master
        self.master.minsize(450,150) #(Height, Width)
        self.master.maxsize(450,150)
        self.master.title("Check files")
        self.master.configure(bg="#F0F0F0")

        self.entry1 = tk.Entry(self.master,width=30,text='')
        self.entry1.grid(row=2,column=1,rowspan=1,columnspan=10,padx=(85,0),pady=(10,0),sticky=W)
        self.entry2 = tk.Entry(self.master,width=30,text='')
        self.entry2.grid(row=4,column=1,rowspan=1,columnspan=10,padx=(85,0),pady=(10,0),sticky=W)
        
        self.btn_browse1 = tk.Button(self.master,width=15,height=1,text='Browse...', command=self.open_file)
        self.btn_browse1.grid(row=2,column=0,padx=(25,0),pady=(10,0),sticky=N+W)
        self.btn_browse2 = tk.Button(self.master,width=15,height=1,text='Browse...', command=self.open_file)
        self.btn_browse2.grid(row=4,column=0,padx=(25,0),pady=(10,0),sticky=N+W)
        self.btn_ckfile = tk.Button(self.master,width=15,height=2,text='Check for files...', command=self.load_file)
        self.btn_ckfile.grid(row=6,column=0,padx=(25,0),pady=(10,0),sticky=N+W)
        self.btn_close = tk.Button(self.master,width=15,height=2,text='Close Program', command=self.close_program)
        self.btn_close.grid(row=6,column=10,padx=(25,0),pady=(10,0),sticky=E+W)

    def load_file(self):
        name = askdirectory()

    def open_file(self):
        name = askopenfilename()

    def close_program(self):
        name = self.master.destroy()
        os._exit(0)

        
if __name__ == "__main__":
    root = tk.Tk()
    root.directory = tkinter.filedialog.askdirectory(parent=root)
    App = ParentWindow(root)
    root.mainloop()
