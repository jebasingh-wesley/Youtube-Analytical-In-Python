from os import remove
from requests_html import HTMLSession
import csv
import pandas as pd
import YoutubeTags
from YoutubeTags import videotags
import re
frequency = {}
mass=[]

#create the session
session = HTMLSession()

#define our URL
url = 'https://www.youtube.com/results?search_query=mohan+hits'

#use the session to get the data
r = session.get(url)

#Render the page, up the number on scrolldown to page down multiple times on a page
r.html.render(sleep=1, keep_page=True, scrolldown=1)

#take the rendered html and find the element that we are interested in
videos = r.html.find('#video-title')

#loop through those elements extracting the text and link
for item in videos:
    video = {
        'title': item.text,
        #'link': item.absolute_links
    }
    #print(video)
    mass.append(video)
    text = mass
    pattern = re.findall(r'\b[a-z]{2,15}\b', str(mass))
    for word in pattern:
        count = frequency.get(word,0)
        frequency[word] = count + 1
    frequency_list = frequency.keys()
    for words in frequency_list:
        print(words, frequency[words])
 




