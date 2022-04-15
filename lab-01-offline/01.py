instr = input("Please, enter a string: ") 

for i in range(1,len(instr),1):
  if instr[i] == instr[0]:
    instr=instr[:i]+'$'+instr[i+1:]

print("Output: " + instr)