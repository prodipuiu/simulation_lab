il1=list(map(int, input("Please, enter a set of numbers(ex: 10,20,30,10,25,20): ").split(',')))
il2=list(map(int, input("Please, enter a set of numbers(ex: 10,20,30,10,25,20): ").split(',')))

list1 = []
list2 = []
list3 = []

for i in range(0, len(il1), 1):
  if i%2!=0:
    list1.append(il1[i])
    list3.append(il1[i])

for i in range(0, len(il2), 1):
  if i%2==0:
    list2.append(il2[i])
    list3.append(il2[i])

print("Element at odd-index positions from list one: ",list1)
print("Element at odd-index positions from list one: ",list2)
print("Printing Final third list: ", list3)