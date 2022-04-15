import matplotlib.pyplot as plt
import math

z1 = [12,7]
z2 = [3,5]
z3 = [2,7]

u1 = []
u2 = []
u3 = []

z = []
u = []

u1.append(z1[0]/16)
u1.append(z1[1]/16)

u2.append(z2[0]/17)
u2.append(z2[1]/17)

u3.append(z1[0]/15)
u3.append(z1[1]/15)

temp = float(0.0)
for i in range(2, 5000, 1):
  temp = ((13*z1[i-1]) + (11*z1[i-2]) + 3)%16
  z1.append(temp)
  u1.append(temp/16)

  temp = ((12*pow(z2[i-1], 2)) + (13*z2[i-2]))%17
  z2.append(temp)
  u2.append(temp/17)

  temp = (pow(z3[i-1], 3) + pow(z3[i-2], 2))%15
  z3.append(temp)
  u3.append(temp/15)

'''print(z1)
print(z2)
print(z3)

print(u1)
print(u2)
print(u3)'''


for i in range(5000):
  z.append(z1[i]+z2[i]+z3[i])

for i in range(5000):
  temp = int(u1[i]+u2[i]+u3[i])
  u.append(u1[i]+u2[i]+u3[i]-temp)

print('Z =',z)
print('U =',u)
#print(len(z))
#print(len(u))


x = []
for i in range(1, 5001, 1):
  x.append(str(i))

plt.bar(x[0:100],z[0:100])
#plt.ylim(0,1)
plt.xlabel("Index of random numbers")
plt.ylabel("Random numbers")
plt.show()

plt.bar(x[0:1000],z[0:1000])
#plt.ylim(0,1)
plt.xlabel("Index of random numbers")
plt.ylabel("Random numbers")
plt.show()

plt.bar(x[0:5000],z[0:5000])
#plt.ylim(0,1)
plt.xlabel("Index of random numbers")
plt.ylabel("Random numbers")
plt.show()
