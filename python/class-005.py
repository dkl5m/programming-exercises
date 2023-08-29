# Dictionaries

"""
Lists: sorted, mutable, and duplicate-valued collection;
Tuples: sorted, immutable, and duplicate-valued collection;
Dictionaries: unordered, immutable collection that does not allow duplicate values;
"""

# index     0       1       2
list1 = ["item2", "item3", "item2"];
tuple1 = ("item2", "item3", "item2");

# key = value
dictionary1 = {"key1" : "King", "key2" : 1994, "key3": True};

dictionary2 = {
    "name": "Bruna",
    "age": 27,
    "nationality": "brazilian"
}
print(dictionary2);

print(dictionary2["age"]);
print(dictionary2.get("age"));
print(dictionary2.keys());
print(len(dictionary2));
print(dictionary2.values());

# IF
if "age" in dictionary2:
    print("The key Age exists!");

print(dictionary2.items());


dictionary3 = {"name": "King", "yearOfBirth": 1998, "logicValue": True};
print(dictionary3);

dictionary3["age"] = 24;
print(dictionary3);

dictionary3.update({"state": "CE"});
print(dictionary3);

# popitem delete last item (version 3.7 above)
# below 3.7, it deletes a random item;
dictionary3.popitem();
print(dictionary3);

dictionary3.pop("yearOfBirth");
print(dictionary3);

del dictionary3["logicValue"];
print(dictionary3);

"""
del dictionary3;
# it will give an error
print(dictionary3);
"""

dictionary3.clear();
print(dictionary3);

dictionary4 = {"name": "King", "yearOfBirth": 1998, "logicValue": True};

# FOR
for x in dictionary4:
    print(x, ":", dictionary4[x]);

for x in dictionary4.values():
    print(x);

for x in dictionary4.keys():
    print(x);

for x, y in dictionary4.items():
    print(x, y);

# COPY
dictionary5 = dictionary4.copy();
print(dictionary5);

dictionary6 = dict(dictionary4);
print(dictionary6);

dictionary4["age"] = 24;
print(dictionary4);
print(dictionary5);
print(dictionary6);

# NONE
x = None;
print(x);

# FROMKEYS
# index     0       1       2
tuple1 = ("item1", "item2", "item3");
dictionary7 = dict.fromkeys(tuple1);
print(dictionary7);

tuple2 = ("item1", "item2", "item3");
tuple3 = ("item1", "item2", "item3");
dictionary8 = dict.fromkeys(tuple2, tuple3);
print(dictionary8);

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
};

print(dictio1);