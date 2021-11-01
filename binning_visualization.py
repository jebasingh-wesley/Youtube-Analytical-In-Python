#BINNING_DATA.csv

import numpy as np
from PIL import Image
from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS

text = open('title.csv', 'r',encoding="utf8").read()
wc = WordCloud(background_color = 'white', width = 1920, height = 1080)
wc.generate_from_text(text)
wc.to_file('most_used_tags.png')




#text = open("title.txt",encoding="utf8").read()
#wordcloud = WordCloud().generate(text)
# Display the generated image:
#plt.imshow(wordcloud)
#plt.axis("off")
#plt.show()



import numpy as np
import pandas as pd
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
from PIL import Image

#text = open("title.txt",encoding="utf8").read()

#wordcloud = WordCloud().generate(text)

# Display the generated image:

#wordcloud = WordCloud(width=500, height=500,prefer_horizontal=0.5,background_color="rgba(255, 255, 255, 0)", mode="RGBA").generate(text)

#plt.imshow(wordcloud)
#plt.axis("off")
#plt.show()
#wordcloud.to_file("img_dir/peace_and_love.png")