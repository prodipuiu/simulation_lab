def prime_or_not(flag):
  count = int(0)

  if flag == 1:
    print("Prime!!!")

  elif flag>1:
    for i in range(1, flag+1, 1):
      if flag%i==0:
        count = count+1

    if count>2:
      print("Non-prime!!!")

    else:
      print("Prime!!!")

    

  else:
    print("Invalid input!!!")







key=int(input("Please, enter an integer number to check whether it's prime or non-prime: "))

prime_or_not(key)