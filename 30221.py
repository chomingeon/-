import csv
import numpy
import matplotlib.pyplot as pit

f=open('C:\\Users\\User\\Downloads\\1.csv')
data=csv.reader(1)
xlabel,y0,y1=[],[],[]

for i, row in enumerate(data)
    if i < 4 :
        continue
    else:
        xlable.append(row[0])
        y0.append(int(row[1]))
        y0.append(int(row[2]))
