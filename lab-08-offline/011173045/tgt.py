import math
import matplotlib.pyplot as plt


b = [1,1,1,1,1]
w = []
u = []
r = 3
q = 5
l = 4

for i in range(5, 1000, 1):
  if b[i-r]==0 and b[i-q]==0:
    temp=0
    b.append(temp)

  elif b[i-r]==1 and b[i-q]==1:
    temp=0
    b.append(temp)

  else:
    temp=1
    b.append(temp)

#print(type(b[3]))
print('b =', b)

for i in range(0, 1000, l):
  bit_segment = b[i:i+l]

  str1 = ''

  for j in bit_segment:
    str1 = str1 + str(j)
    
  #print(str1)

  w.append(int(str1, 2))
  temp2 = int(str1,2)/pow(2,l)
  u.append(temp2)

print('w =', w)
print("u =", u)

count = 0
for i in range(1, 2**l, 1):
  if w[i]==w[0]:
    print("CYCLE DETECTED!!!")

x = []
j = 1
for i in range(1,len(u)+1, 1):
  x.append(str(i))

plt.bar(x,u)
plt.ylim(0,1)
plt.xlabel("Index of a random number, i")
plt.ylabel("The random number Ui")
plt.show()
