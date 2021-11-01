#str =(open('title.txt',encoding='utf-8').read())
from collections import Counter

data_set = (open('title.txt',encoding='utf-8').read())

split_it = data_set.split()

Counter = Counter(split_it)

most_occur = Counter.most_common(6)

print(most_occur)
