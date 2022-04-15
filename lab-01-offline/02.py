instr = input("Please, enter a string: ")
temp = instr

j = len(instr)-1
flag = int(0);

for i in  range(0, len(instr), 1):
  if instr[i] != temp[j]:
    flag=1
  
  j = j-1

if flag==0:
  print(""+instr+" is palindrome.") 

else:
  print(""+instr+" is not palindrome.") 