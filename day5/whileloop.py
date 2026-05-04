#LOOPS
# loops are used to repeat instructions until a certain condition is met

#while loop
# while condition:
#     # code to be executed

# count = 1
# while count <= 5:
#     print(count)
#     count += 1
# 


# i = 100
# while i >=1:
#     print(i)
#     i = i-1
   
# print the multiplication table of number n

# i = 1
# n = int(input("Enter a number to print its multiplication table:"))
# while i <=10:
#     print(n*i)
#     i+= 1

#print the element of the following list using a loop
# [1,2,3,4,5]

# i = 0
# list = [1, 2, 3, 4, 5]
# while i < len(list):
#     print(list[i])
#     i += 1


nums = [1, 2, 3, 4, 5]

x = 4

i = 0
while i < len(nums):
    if nums[i] == x:
        print("Element found at index", i)
        break
    i += 1
