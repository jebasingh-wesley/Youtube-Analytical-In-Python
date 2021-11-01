from os import remove
from requests_html import HTMLSession
import csv
import pandas as pd
import YoutubeTags
from YoutubeTags import videotags
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
    mass.append(item.text)
df = pd.DataFrame(mass)
csv_data = df.to_csv(index=False)
df.to_csv('title.csv', index=False)



    #with open('TITLE.txt', 'w',encoding='utf-8') as f:
        #for item in mass:
            #f.write("%s\n" % item)




 

