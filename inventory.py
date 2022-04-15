import random
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)


m = int(input("Insert max storage capacity : "))
n = int(input("Insert cycle length : "))

binventory = int(3) #b-beginning
demand = int(0)
einventory = int(0) #e-ending
sq = int(0)  #shortage quantity
oq = int(8) #order quantity
arrivesin = int(2)
arrivesin = arrivesin-1
arrive_count = int(0)   #-1 hobar pore jeno ekbar e kaj kre
scount = int(0) #s-shortage
eicount = int(0)    #ending
dcount = int(0) #d-day
eiarray = []    #ei-ending inventory
one_time_use = 1    #1st cycle er order handeling er jonno



for cycle in range(1,6,1):
    print("Cycle :", cycle)
    print("---------------------------------------------------------------------------------------------------")
    for day in range(1, n+1, 1):

        demand = np.random.choice(a=[0,1,2,3,4], p=[0.10, 0.25, 0.35, 0.21, 0.09])
        #print("demand",demand)

        if arrivesin==-1 and one_time_use==1:
            one_time_use=0
            if oq>=sq:
                binventory = 8-sq
            sq = 0

        if arrivesin==-1 and arrive_count==1:
            arrive_count=0 #inventory mtro dhuklo
            binventory = m
            sq = 0

        if day == n:
            arrivesin = np.random.choice(a=[1,2,3], p=[0.6, 0.3, 0.1])
            arrive_count=1  #inventory order kora hoiche, on the way
            #print("arrivesin",arrivesin)

        if demand+sq<binventory:
            einventory = binventory-demand
            sq = 0

        else:
            sq = demand+sq-binventory
            einventory = 0

        if arrivesin>-1:
            print("Day :", day, "BI :", binventory, "Demand :", demand, "EI :", einventory, "Shortage :", sq, "Arrivesin :", arrivesin)

        else:
            print("Day :", day, "BI :", binventory, "Demand :", demand, "EI :", einventory, "Shortage :", sq, "Arrivesin : -")

        binventory = einventory

        if sq>0:
            scount = scount+1

        if arrivesin>=0:
            arrivesin = arrivesin-1

        eicount = eicount+einventory
        dcount = dcount+1
        eiarray.append(einventory)

    print("---------------------------------------------------------------------------------------------------")

print("Average ending inventory :", eicount/dcount)
print("No of days shortage occurs :", scount)

z = []
for i in range(1, dcount+1):
    z.append(str(i))

plt.bar(z,eiarray)
plt.ylim(0,11)
plt.xlabel("No of Days")
plt.ylabel("Ending Inventory")
plt.show()

