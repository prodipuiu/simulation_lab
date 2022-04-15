import matplotlib.pyplot as plt 

x = [1,2,3,4,5,6]
y = [9200,6100,9550,8870,7760,7490]

plt.scatter(x, y, color="green", label = "Moisturizer")
plt.xlabel("Month No")
plt.ylabel("Sales")
plt.legend() 
plt.show() 