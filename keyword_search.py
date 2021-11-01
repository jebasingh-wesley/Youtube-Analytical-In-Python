from tkinter import *
from bs4 import BeautifulSoup
import tkinter as tk
from bs4.element import ProcessingInstruction, Tag
import requests


root = tk.Tk()
root.geometry('1000x900')
root.resizable(0,0)
root.title("YouTube Keyword Scraper")
Label(root, text ='YouTube Keyword Scraper' , font ='arial 20 bold').pack()
Label(root, text ='Enter URL :' , font ='arial 13 bold').place(x=5 ,y=100)
Websites = Text(root,font = 'arial 10',height='5', width = '80')
Websites.place(x= 140,y = 60)
T = Text(root,font = 'arial 10', height='20', width='100')
T.place(x=50 ,y=500)


def extract():
    r = requests.get(Websites.get(1.0,END))
    soup = BeautifulSoup(r.content, "html")
    
    title = soup.title.string
    print ('TITLE IS :', title)
    
    

    meta = soup.find_all('meta')
    for tag in meta:
        
        if 'name' in tag.attrs.keys() and tag.attrs['name'].strip().lower() in ['keywords']:
            T.insert(tk.END, tag.attrs['content'])

            
        


block = Button(root, text = 'Submit',font = 'arial 12 bold',pady = 5,command = extract ,
width = 6, bg = 'royal blue', activebackground = 'sky blue')
block.place(x = 230, y = 250)
root.mainloop()
