inlist=list(map(int, input("Please, enter a set of integer numbers(ex: 10,20,30,10,25,20): ").split(',')))
flag = []

even=int(0)
odd=int(0)

for i in inlist:
  if i%2==0:
    even=even+1

  else:
    flag.append(i)
    odd=odd+1

  
print("Even count = ", even)
print("Odd count = ", odd)
print("Updated list: ", flag)