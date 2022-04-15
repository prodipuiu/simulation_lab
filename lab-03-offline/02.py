import random
import matplotlib.pyplot as plt
import math

random.seed(0)

trials=[100, 1000, 5000, 10000]
hits=int(0)

areaofcurve=[]
areaofrec=float(0.0)
areaofrec=3*5

x1=[]
y1=[]
x2=[]
y2=[]

for i in trials:
  for j in range(i):
    x=random.uniform(0,3)
    y=random.uniform(0,5)

    temp1=x+2

    if temp1>=y:
      hits=hits+1
      x1.append(x)
      y1.append(y)

    else:
      x2.append(x)
      y2.append(y)

  

  temp2=(hits/i)*areaofrec
  print("For",i,"trials area under the curve(y=x+2) =", temp2)

  hits=0


  plt.scatter(x1, y1, color="red", label="Under/n the curve y=x+2")
  plt.scatter(x2, y2, color="green", label="Above the curve y=x+2")
  plt.xlabel('X-axis')
  plt.ylabel('Y-axis')
  plt.legend() 
  plt.show()