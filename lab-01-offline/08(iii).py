import matplotlib.pyplot as plt 

x = [1,2,3,4,5,6]
y1 = [2500,2630,2140,3400,3600,2760] 
y2 = [1500,1200,1340,1130,1740,1555] 
y3 = [5200,5100,4550,5870,4560,4890] 
y4 = [9200,6100,9550,8870,7760,7490] 
y5 = [1200,2100,3550,1870,1560,1890]

total_sale_per_month = []

for i in range(0, len(x), 1):
  total_sale_per_month.append(y1[i]+y2[i]+y3[i]+y4[i]+y5[i])


plt.bar(x,total_sale_per_month)
plt.xlabel("Month No")
plt.ylabel("Total Sales In Each Month")

plt.title('Total number of sales each month')
plt.show()