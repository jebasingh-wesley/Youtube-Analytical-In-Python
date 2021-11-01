#str =(open('title.txt',encoding='utf-8').read())
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt



dictionary = {}
data_set = (open('title.txt',encoding='utf-8').read())
split_it = data_set.split()
Counter = Counter(split_it)
most_occur = Counter.most_common(5)
#print(most_occur)
def Convert(tup, di):
    for a, b in tup:
        di.setdefault(a, b)
    return di
data=(Convert(most_occur, dictionary))
#print(data)
courses = list(data.keys())
values = list(data.values())
  
fig = plt.figure(figsize = (10, 5))
 

plt.bar(courses, values, color ='maroon',
        width = 0.4)
 
plt.xlabel("Courses offered")
plt.ylabel("No. of students enrolled")
plt.title("Students enrolled in different courses")
plt.show()




