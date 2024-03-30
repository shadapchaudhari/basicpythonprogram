num = 11
flag = True  # Initialize flag as True
sum = 0      # Initialize sum as 0
if num == 1:
    print(num , "is not a prime number")
elif num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = False  # Set flag to False if a divisor is found
            sum += i      # Add the divisor to sum
            break         # Exit the loop once a divisor is found
    if flag:
        print(num , "is a prime number")
    else:
        print(num , "is not a prime number")
        print("Sum of divisors:", sum)  # Print the sum of divisors
