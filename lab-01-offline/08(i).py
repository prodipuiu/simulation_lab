import matplotlib.pyplot as plt 
# line 1 points 
x = [1,2,3,4,5,6]
y1 = [2500,2630,2140,3400,3600,2760] 
 
# plotting the line 1 points  
plt.plot(x, y1, color= 'blue',label = "Toothpaste") 
  
# line 2 points 
y2 = [1500,1200,1340,1130,1740,1555] 
# plotting the line 2 points  
plt.plot(x, y2, color= 'orange',label = "Facewash") 

# line 3 points 
y3 = [5200,5100,4550,5870,4560,4890] 
# plotting the line 3 points  
plt.plot(x, y3, color= 'green',label = "Shampoo") 

# line 4 points 
y4 = [9200,6100,9550,8870,7760,7490] 
# plotting the line 4 points  
plt.plot(x, y4, color= 'red',label = "Moisturizer") 

# line 5 points 
y5 = [1200,2100,3550,1870,1560,1890] 
# plotting the line 5 points  
plt.plot(x, y5, color= 'purple',label = "Soap") 
  
# naming the x axis 
plt.xlabel('Month No') 
# naming the y axis 
plt.ylabel('Salse') 
# giving a title to my graph 
plt.title('6 Month’s sales data for different products') 
  
# show a legend on the plot 
plt.legend() 
  
# function to show the plot 
plt.show() 