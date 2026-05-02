# Wap to ask the user to enter 3 names of their 3 fav movies and store them in a list

# movies = []

# movie1 = input("enter movie 1:")
# movie2 = input("enter movie 2:")
# movie3 = input("enter movie 3:")

# movies.append(movie1)
# movies.append(movie2)
# movies.append(movie3)

# print("Your 3 favourite movies are:", movies)


# wap to check if a list contains a palindrome of element 

# list = [1,2,3,2,1,2]

# copy_list = list.copy()
# copy_list.reverse()
# if copy_list == list:
#     print("the list is a palindrome")
# else:
#     print("the list is not a palindrome")


# wap to count the number of students with ths A grade in the tuple

grades = ('A', 'B', 'C', 'A', 'D', 'A', 'B')

count = grades.count('A')
print("Number of students with grade A:", count)

grades_list = list(grades)
print(grades_list)

grades_list.sort()
print(grades_list)

graded_tuple = tuple(grades_list)
print(graded_tuple)