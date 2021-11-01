import matplotlib.pyplot as plt
import csv

x = []
y = []


with open('/home/ubuntu/Documents/g4g.csv','r') as csvfile:
	lines = csv.reader(csvfile, delimiter=',')
	for row in lines:
		x.append(row[2])
		y.append(int(row[3]))
        
a = [x]
b = [y]


