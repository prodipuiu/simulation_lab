inlist=list(map(int, input("Please, enter a set of numbers(ex: 10,20,30,10,25,20): ").split(',')))

flag=[]

for i in inlist:
  if i not in flag:
    flag.append(i)
  


print(flag)