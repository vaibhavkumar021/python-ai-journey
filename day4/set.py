# Sets is the collection of the unordered items
#Each element in the set must be unique and immutable 

# nums ={1,2,3,3,4,5,7}
# set2 = {1,2,2,2,}

# repeated elements stored only once ,so it resolved to {1,2}

#null_set =set() # empty set syntax


# collection = {1,2,3,4}
# collection1 = {1,5,3,9}

# print(collection)
# print(type(collection))

# collection.add(5)
# print(collection)

# collection.remove(2)
# print(collection)

# collection.clear()
# print(collection)


# collection.pop()
# print(collection)

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# union of two sets
union_set = set1.union(set2)
print(union_set)

# intersection of two sets
print(set1.intersection(set2))