import re
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


frequency = {}
X=[]
Y=[]
#Open the sample text file in read mode.
document_text = open('title.txt', 'r',encoding='utf-8')
#convert the string of the document in lowercase and assign it to text_string variable.
text = document_text.read().lower()
pattern = re.findall(r'\b[a-z]{2,15}\b', text)
for word in pattern:
     count = frequency.get(word,0)
     frequency[word] = count + 1
frequency_list = frequency.keys()
for words in frequency_list:
    X.append(words)
    #Y.append(frequency[words])

#print(X)
#print(Y)
nme = [X]
#deg = [Y]
#dict = {'NAME': nme, 'COUNT': deg}	
#df = pd.DataFrame(dict)
#df.to_csv('BINNING_DATA.csv')

nme = [X]
for dict in nme:
    print(dict) 
    df = pd.DataFrame(dict)
    df.to_csv('BINNING_DATA.csv')










