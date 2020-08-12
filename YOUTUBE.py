from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from pytube import YouTube
import os
def note():
	messagebox.showinfo("HOW TO DOWNLOAD","Steps : \n 1,ENTER link of YouTube video \n 2, select path to download the video")
root = Tk()
root.title("YouTube downloader")
canvas = Canvas(width=500,height=100)
canvas.pack()
frame = Frame()

frame.place(relx=0.3,rely=0.1,relwidth=0.9,relheight=0.8)

label = Label(frame,text="ENTER LINK",font=("bold",10))
label.grid(row=1,column=0)
mylink=StringVar()
Link= Entry(frame,textvariable=mylink)
Link.grid(row=1,column=1)
def browse():
	select_path= filedialog.askdirectory(initial="select download path")
	selector_path.set(select_path)
def url_fetch():
    x=str(mylink.get())
    video=YouTube(x).streams.filter(progressive=True,file_extension='mp4').order_by('resolution').desc().first()
    mys= selector_path.get()
    video.download(mys)
    messagebox.showinfo("SUCCESSFULLY", 
						"DOWNLOADED AND SAVED")
selector_path=StringVar()
button = Button(frame,text="download",bg="black",fg="gold",command=lambda:url_fetch())
button.grid(row=1,column=2)
button = Button(frame,text="select path",bg="black",fg="gold",command=browse)
button.grid(row=3,column=1)
note()
root.mainloop()