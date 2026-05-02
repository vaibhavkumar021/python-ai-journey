# A buit-in data type that stores set of values
# it can store elements of different types(integer,float,string,boolean)

# marks = [90, 85, 78, 92, 88]
# student = ["alice", 76,"delhi"]
# sudent[0] = "bob" allowed in python
# len(student) returns length

list = [1, 2, 3, 4, 5]
print(list)  # prints the entire list

list.append(8)
print(list)  # prints the modified list
list.sort()
print(list)  # prints the modified list
list.sort(reverse=True)
print(list)  # prints the modified list

list.reverse()
print(list)  # prints the modified list
list.insert(2,10)
print(list)  # prints the modified list

list.remove(3)
print(list)  # prints the modified list

list.pop(4)
print(list)  # prints the modified list