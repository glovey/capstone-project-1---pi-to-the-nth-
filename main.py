import math



from mpmath import mp
mp.dps = 21000    

num = str((mp.pi))

user = input("how many decimal places would youlik to print pi to? enter a number from 0 - 1000 \n")
dec = int(user) + 2

if user == "0":
  print (3)
else:
  print (num[0:dec])
