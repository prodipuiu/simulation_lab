#Name: Md Sezan Mahmud Saikat
#ID: 011 173 045

import math
import matplotlib.pyplot as plt

ax = [] #x coordinate of car 'A'
ay = [] #y coordinate of car 'A'
bx = [] #x coordinate of car 'B'
by = [] #y coordinate of car 'B'
cx = [] #x coordinate of car 'C'
cy = [] #y coordinate of car 'C'
dx = [] #x coordinate of car 'D'
dy = [] #y coordinate of car 'D'

distBetweenC_A = float(0.0)
distBetweenB_C = float(0.0)
distBetweenD_B = float(0.0)
distBetweenA_D = float(0.0)

av = 3.0
bv = 5.0
cv = 7.0
dv = 2.0


timeLimit = 20

for i in range(0, timeLimit+1, 1):
    if i==0:

        ax.append(10)
        ay.append(0)
        bx.append(0)
        by.append(10)
        cx.append(10)
        cy.append(10)
        dx.append(0)
        dy.append(0)

        print("\nAt time=", i)
        print("x_A =", ax[i], "y_A =", ay[i])
        print("x_B =", bx[i], "y_B =", by[i])
        print("x_C =", cx[i], "y_C =", cy[i])
        print("x_D =", dx[i], "y_D =", dy[i])

        distBetweenC_A = (math.sqrt(pow((cx[i]-ax[i]), 2) + pow((cy[i]-ay[i]), 2)))
        distBetweenD_B = (math.sqrt(pow((dx[i]-bx[i]), 2) + pow((dy[i]-by[i]), 2)))
        distBetweenB_C = (math.sqrt(pow((bx[i]-cx[i]), 2) + pow((by[i]-cy[i]), 2)))
        distBetweenA_D = (math.sqrt(pow((ax[i]-dx[i]), 2) + pow((ay[i]-dy[i]), 2)))

        print("\nD to B Distance =", distBetweenD_B)
        print("C to A Distance =", distBetweenC_A)
        print("B to C Distance =", distBetweenB_C)
        print("A to D Distance =", distBetweenA_D)


    else:
        sin = (cy[i-1]-ay[i-1])/distBetweenC_A
        cos = (cx[i-1]-ax[i-1])/distBetweenC_A
        ax.append(ax[i-1] + (av*cos))
        ay.append(ay[i-1] + (av*sin))

        sin = (by[i-1]-cy[i-1])/distBetweenB_C
        cos = (bx[i-1]-cx[i-1])/distBetweenB_C
        cx.append(cx[i-1] + (cv*cos))
        cy.append(cy[i-1] + (cv*sin))

        sin = (dy[i-1]-by[i-1])/distBetweenD_B
        cos = (dx[i-1]-bx[i-1])/distBetweenD_B
        bx.append(bx[i-1] + (bv*cos))
        by.append(by[i-1] + (bv*sin))

        sin = (ay[i-1]-dy[i-1])/distBetweenA_D
        cos = (ax[i-1]-dx[i-1])/distBetweenA_D
        dx.append(dx[i-1] + (dv*cos))
        dy.append(dy[i-1] + (dv*sin))


        print("\nAt time=",i)
        print("x_A =", ax[i], "y_A =", ay[i])
        print("x_B =", bx[i], "y_B =", by[i])
        print("x_C =", cx[i], "y_C =", cy[i])
        print("x_D =", dx[i], "y_D =", dy[i])

        distBetweenC_A = (math.sqrt(pow((cx[i]-ax[i]), 2) + pow((cy[i]-ay[i]), 2)))
        distBetweenD_B = (math.sqrt(pow((dx[i]-bx[i]), 2) + pow((dy[i]-by[i]), 2)))
        distBetweenB_C = (math.sqrt(pow((bx[i]-cx[i]), 2) + pow((by[i]-cy[i]), 2)))
        distBetweenA_D = (math.sqrt(pow((ax[i]-dx[i]), 2) + pow((ay[i]-dy[i]), 2)))

        print("\nD to B Distance =", distBetweenD_B)
        print("C to A Distance =", distBetweenC_A)
        print("B to C Distance =", distBetweenB_C)
        print("A to D Distance =", distBetweenA_D, "\n")

        if distBetweenD_B<5:
            print("Car B shoots car D at time =", i)

        if distBetweenC_A<5:
            print("Car A shoots car C at time =", i)

        if distBetweenB_C<5:
            print("Car C shoots car B at time =", i)

        if distBetweenA_D<5:
            print("Car D shoots car A at time =", i)




plt.plot(ax, ay, color= 'blue',label = "Path A") 
plt.plot(bx, by, color= 'orange',label = "Path B") 
plt.plot(cx, cy, color= 'green',label = "Path C") 
plt.plot(dx, dy, color= 'red',label = "Path C") 
  
plt.xlabel('X-axis') 
plt.ylabel('Y-axis') 

plt.title('Position of the cars between time 0-20 unit time') 

plt.legend() 
plt.show() 