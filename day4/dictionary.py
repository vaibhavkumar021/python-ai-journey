# Dictionaries are used to store data values in key:value pairs.
# they are unordered,mutable(cahngeable) and don't allow duplicate keys

info = {
    "key" : "value",
    "name" : "vaibhav",
    "learning" : "python",
    "age" : 20,
    "is_student": True,
    "marks" : [90, 85, 78]


}

print(info)

info.keys()  # returns all the keys in the dictionary
info.values()  # returns all the values in the dictionary
info.items()  # returns all the key-value pairs in the dictionary
info.get("key")  # returns the value associated with the key
info.update({"name":"bob"})  # updates the value of the key
print(info)