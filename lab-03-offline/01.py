import random
import matplotlib.pyplot as plt
import math

random.seed(0)

trials=[100, 1000, 5000, 10000]
hits=int(0)
pi_array=[]

x1=[]
y1=[]
x2=[]
y2=[]
e=[]
area=[]
pivalue=[]

for i in trials:
  for j in range(i):
    x=random.uniform(0,4)
    y=random.uniform(0,4)

    dis=math.sqrt(((x-2)*(x-2))+((y-2)*(y-2)))

    if dis<=1.5:
      x1.append(x)
      y1.append(y)
      hits=hits+1

    else:
      x2.append(x)
      y2.append(y)

  pi=7.111111111*(hits/i)
  pivalue.append(pi)
  area.append(pi*1.5*1.5)
  print("For",i,"trials value of pi = ", pi)
  temp=(3.1416-pi)

  if temp<0:
    e.append(temp*(-1))

  else:
    e.append(temp)

  plt.scatter(x1, y1, color="red", label="Hits")
  plt.scatter(x2, y2, color="green", label="Misses")

  plt.legend()
  plt.show()
  x1.clear()
  x2.clear()
  y1.clear()
  y2.clear()


  


  hits=0


z=["100", "1000", "5000", "10000"]
plt.bar(z,pivalue)
plt.ylim(3,3.5)
plt.xlabel("Trials")
plt.ylabel("Pi-Value")
plt.show()

plt.bar(z,e)
plt.ylim(0,0.3)
plt.xlabel("Trials")
plt.ylabel("Error")
plt.show()

plt.bar(z,area)
plt.ylim(6,8)
plt.xlabel("Trials")
plt.ylabel("Area")
plt.show()