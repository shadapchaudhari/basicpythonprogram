#write a python programm to print given no is reverse
n = int(input("enter number"))
rev = 0
while n > 0:
      rev = (rev*10)+n%10
      n=n//10
print("reverse=",rev)