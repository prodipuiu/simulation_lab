#Name: Md Sezan Mahmud Saikat
#ID: 011 173 045
#Buffon's Needle for d=2 and l=4
import math
import random
import matplotlib.pyplot as plt 
x=input("Enter d: ")
y=input("Enter l: ")
d=int(x)
l=int(y)
random.seed(1)
hits=0
n=10000
x1=[]
y1=[]
x2=[]
y2=[]
for i in range(0,n,1):
  D=random.uniform(0,d/2)
  theta=random.uniform(0,3.1416)
  if D<=(l/2)*math.sin(theta):
    x1.append(theta)
    y1.append(D)
    hits=hits+1

  else:
    x2.append(theta)
    y2.append(D)

pi=((2*l)/d)*(n/hits)

print(pi)

plt.scatter(x1, y1, color="red")
plt.scatter(x2, y2, color="green")
plt.xlabel("0<=theta<=180")
plt.ylabel("0<=D<=d/2")