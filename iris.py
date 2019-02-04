text_file = open("file.txt", "r")
lines = text_file.readlines()
for i in range(len(lines)):
    lines[i]=lines[i].split(',')

for i in range(len(lines)):
    for j in range(4):
        lines[i][j]=float(lines[i][j])

x1=[]
y1=[]
x2=[]
y2=[]
x3=[]
y3=[]
for i in lines:
    if i[4]=='Iris-setosa\n':
        x1.append(i[0])
        y1.append(i[1])
    if i[4]=='Iris-versicolor\n':
        x2.append(i[0])
        y2.append(i[1])
    if i[4]=='Iris-virginica\n':
        x3.append(i[0])
        y3.append(i[1])
from matplotlib import pyplot as plt    
plt.plot(x1, y1, 'bo', x2, y2, 'ro',x3, y3, 'go',)
plt.show()
