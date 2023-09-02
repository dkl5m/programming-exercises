# Dictionaries

"""
Lists: sorted, mutable, and duplicate-valued collection;
Tuples: sorted, immutable, and duplicate-valued collection;
Dictionaries: unordered, immutable collection that doesnt
    allow duplicate values;
Sets: unordered, immutable collection that does not allow duplicate
    values;
"""

"""
# index     0       1       2
list1 = ["item2", "item3", "item2"]
tuple1 = ("item2", "item3", "item2")

# key = value
dictionary1 = {"key1": "King", "key2": 1994, "key3": True}

dictionary2 = {
    "name": "Bruna",
    "age": 27,
    "nationality": "brazilian"
}
print(dictionary2)

print(dictionary2["age"])
print(dictionary2.get("age"))
print(dictionary2.keys())
print(len(dictionary2))
print(dictionary2.values())

# IF
if "age" in dictionary2:
    print("The key Age exists!")

print(dictionary2.items())


dictionary3 = {"name": "King", "yearOfBirth": 1998, "logicValue": True}
print(dictionary3)

dictionary3["age"] = 24
print(dictionary3)

dictionary3.update({"state": "CE"})
print(dictionary3)

# popitem delete last item (version 3.7 above)
# below 3.7, it deletes a random item;
dictionary3.popitem()
print(dictionary3)

dictionary3.pop("yearOfBirth")
print(dictionary3)

del dictionary3["logicValue"]
print(dictionary3)

# del dictionary3;
# print(dictionary3); # it will give an error


dictionary3.clear()
print(dictionary3)

dictionary4 = {"name": "King", "yearOfBirth": 1998, "logicValue": True}

# FOR
for x in dictionary4:
    print(x, ":", dictionary4[x])

for x in dictionary4.values():
    print(x)

for x in dictionary4.keys():
    print(x)

for x, y in dictionary4.items():
    print(x, y)

# COPY
dictionary5 = dictionary4.copy()
print(dictionary5)

dictionary6 = dict(dictionary4)
print(dictionary6)

dictionary4["age"] = 24
print(dictionary4)
print(dictionary5)
print(dictionary6)

# NONE
x = None
print(x)

# FROMKEYS
# index     0       1       2
tuple1 = ("item1", "item2", "item3")
dictionary7 = dict.fromkeys(tuple1)
print(dictionary7)

tuple2 = ("item1", "item2", "item3")
tuple3 = ("item1", "item2", "item3")
dictionary8 = dict.fromkeys(tuple2, tuple3)
print(dictionary8)

# NESTING
dictio1 = {
    "dictio2": {
        "name": "Ana",
        "age": 25
    },
    "dictio3": {
        "name": "Dick",
        "age": 28,
        "dictio4": {
            "name": "Larissa",
            "age": 6
        }
    },
}

print(dictio1)
"""

# SETS

set1 = {"item1", "Sao Paulo", 4.7, True, 3}
print(type(set1))
print(set1)
print(len(set1))

tuple1 = (3, 7, 9, 5)
set2 = set(tuple1)
print(set2)
print(type(set2))

set3 = set((3, 6, 9, 5))
print(set3)
print(type(set3))


# Accessing the set items
set4 = {3, 6, 9, 5}
# print(set5[0]); cant utilize ref or change the value, because its immutable
# and unordered

for x in set4:
    print(x)
# thats the way to print the elements of a set

print(6 in set4)
print(11 in set4)

# Adding in sets
set5 = {"item1", "item2", "item3", "item4"}
print(set5)
set5.add("item5")
print(set5)
set5.add(8)
set5.add(True)
print(set5)

set6 = {4, 5, 6, 7}
set7 = {"item1", "item2"}

set6.update(set7)
print(set6)
set6.update({"item3", 8})
print(set6)
# update can pass other collection to the set
set6.update(["item3", 3, 8, "item1"])

# list
print(set6)
set6.update(("item4", 3, 8, "item1"))
# tuple
print(set6)

# Removing in set
set6.pop()
# remove random item
print(set6)

set6.remove("item4")
# remove the specified item, but get you an
# error if the element doesnt exist
print(set6)

set6.discard("item2")
# remove the specified item, but doesnt get
# you an error if the element doesnt exist
print(set6)

del set6
# delete set, but give you an error if you try to print it
# print(set6);
set6 = {"item4", 3, 8, "item1"}
set6.clear()
# delete set, but doesnt give you an error if you try
# to print it
print(set6)


# principle functions in set

set8 = {1, 2, 3, 4}
set9 = {5, 6, 7}

# union function
set10 = set8.union(set9)
print(set10)

# intersection function
set11 = {1, 2, 5, 7}
set12 = set8.intersection(set11)
print(set12)

# or

set8.intersection_update(set11)
print(set8)

set13 = {1, 2, 5, 7}
set14 = set8.symmetric_difference(set13)
print(set14)

# or

set8.symmetric_difference_update(set11)
print(set8)
