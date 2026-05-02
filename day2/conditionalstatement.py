# wap to check if a numbre entered by user is odd or even

num = int(input("Enter a number:"))
if num % 2 == 0:
    print(num, "is an even number.")
else:
    print(num, "is an odd number.")


# wap to find the greatest of 3 numbers enterend by ths user

num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))
num3 = float(input("Enter third number:"))

if num1 >= num2 and num1 >= num3:
    print(num1, "is the greatest number.")
elif num2 >= num1 and num2 >= num3:
    print(num2, "is the greatest number.")
else:
    print(num3, "is the greatest number.")

# wap to check if a number is a multiple of 7 or not

num4 = int(input("Enter a number:"))
if num4 % 7 == 0:
    print(num4, "is a multiple of 7.")
else:
    print(num4, "is not a multiple of 7.")