#write a python programm to check the no is palindrome or not
num = int(input("enter a number"))
temp = num
sum = 0
while num > 0:
    r = num % 10
    sum = sum * 10 + r
    num = num // 10
    if temp == sum :
        print("number is palindrome")
    else:
        print("number is not palindrome")


