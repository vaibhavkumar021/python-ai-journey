# Block of statement that perform a specific task

# def func_name(param 1, param 2)
# some work
# return val
# func_name(arg1,arg2) # function call

# def sum(a,b):
#     s = a+b
#     return s

# print(sum(3,4))

# waf to print the length of a list (list is the parameter)

cities = ["delhi", "mumbai", "kolkata", "chennai"]
heros = ["ironman", "thor", "hulk", "captain america"]

# def print_len(list):
#     print(len(list))

# def print_list(list):
#     for item in list:
#         print(item,end=" ")

# print_list(cities)
# print()
# print_list(heros)
# print()



# waf to find the factorial of a number

# x = int(input("Enter a number to find its factorial:"))

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)

# print(factorial(x))




# waf to convert usd to inr

def usd_to_inr(usd):
    inr = usd * 82.5
    return inr

usd_amount = float(input("Enter amount in USD:"))
inr_amount = usd_to_inr(usd_amount)
print(f"Amount in INR: {inr_amount}")