#write a python program to print factorial of given number
i = int (input("enter number"))
fac = 1
while i > 0:
    fac = fac*i
    i=i-1
    print ("factorial=", fac)