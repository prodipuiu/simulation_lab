array1 = [
            [0,1,0,0,0],
            [0,0,1,0,0],
            [0,1,1,0,1],
            [0,1,0,0,1],
            [0,0,0,0,0]
        ]

array2 = [
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0]
        ]

count = int(0)

for i in range(21):
    for j in range(5):
        for k in range(5):
            if i%2==0:
                if array1[j][k]==0:
                    if j-1>=0:
                        if array1[j-1][k]==1:
                            count = count+1

                    if j-1>=0 and k+1<5:
                        if array1[j-1][k+1]==1:
                            count = count+1

                    if k+1<5:
                        if array1[j][k+1]==1:
                            count = count+1

                    if j+1<5 and k+1<5:
                        if array1[j+1][k+1]==1:
                            count = count+1

                    if j+1<5:
                        if array1[j+1][k]==1:
                            count = count+1

                    if j+1<5 and k-1>=0:
                        if array1[j+1][k-1]==1:
                            count = count+1

                    if k-1>=0:
                        if array1[j][k-1]==1:
                            count = count+1

                    if j-1>=0 and k-1>=0:
                        if array1[j-1][k-1]==1:
                            count = count+1

                    if count==3:
                        array2[j][k]=1

                    else:
                        array2[j][k]=0

                    count = int(0)





                elif array1[j][k]==1:
                    if j-1>=0:
                        if array1[j-1][k]==1:
                            count = count+1

                    if j-1>=0 and k+1<5:
                        if array1[j-1][k+1]==1:
                            count = count+1

                    if k+1<5:
                        if array1[j][k+1]==1:
                            count = count+1

                    if j+1<5 and k+1<5:
                        if array1[j+1][k+1]==1:
                            count = count+1

                    if j+1<5:
                        if array1[j+1][k]==1:
                            count = count+1

                    if j+1<5 and k-1>=0:
                        if array1[j+1][k-1]==1:
                            count = count+1

                    if k-1>=0:
                        if array1[j][k-1]==1:
                            count = count+1

                    if j-1>=0 and k-1>=0:
                        if array1[j-1][k-1]==1:
                            count = count+1

                    if count<2:
                        array2[j][k]=0
                    
                    elif count==2 or count==3:
                        array2[j][k]=1

                    elif count>3:
                        array2[j][k]=0

                    count = 0
                

            else:
                if array2[j][k]==0:
                    if j-1>=0:
                        if array2[j-1][k]==1:
                            count = count+1

                    if j-1>=0 and k+1<5:
                        if array2[j-1][k+1]==1:
                            count = count+1

                    if k+1<5:
                        if array2[j][k+1]==1:
                            count = count+1

                    if j+1<5 and k+1<5:
                        if array2[j+1][k+1]==1:
                            count = count+1

                    if j+1<5:
                        if array2[j+1][k]==1:
                            count = count+1

                    if j+1<5 and k-1>=0:
                        if array2[j+1][k-1]==1:
                            count = count+1

                    if k-1>=0:
                        if array2[j][k-1]==1:
                            count = count+1

                    if j-1>=0 and k-1>=0:
                        if array2[j-1][k-1]==1:
                            count = count+1

                    if count==3:
                        array1[j][k]=1

                    else:
                        array1[j][k]=0

                    count = int(0)





                elif array2[j][k]==1:
                    if j-1>=0:
                        if array2[j-1][k]==1:
                            count = count+1

                    if j-1>=0 and k+1<5:
                        if array2[j-1][k+1]==1:
                            count = count+1

                    if k+1<5:
                        if array2[j][k+1]==1:
                            count = count+1

                    if j+1<5 and k+1<5:
                        if array2[j+1][k+1]==1:
                            count = count+1

                    if j+1<5:
                        if array2[j+1][k]==1:
                            count = count+1

                    if j+1<5 and k-1>=0:
                        if array2[j+1][k-1]==1:
                            count = count+1

                    if k-1>=0:
                        if array2[j][k-1]==1:
                            count = count+1

                    if j-1>=0 and k-1>=0:
                        if array2[j-1][k-1]==1:
                            count = count+1

                    if count<2:
                        array1[j][k]=0
                    
                    elif count==2 or count==3:
                        array1[j][k]=1

                    elif count>3:
                        array1[j][k]=0

                    count = 0

    print("-------------------------------------\nTime -",i)
    for p in range(5):
        if i%2==0:
            print(array1[p][0], array1[p][1], array1[p][2], array1[p][3], array1[p][4])

        else:
            print(array2[p][0], array2[p][1], array2[p][2], array2[p][3], array2[p][4])
        
    print("-------------------------------------")
