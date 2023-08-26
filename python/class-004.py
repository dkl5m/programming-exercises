# CHANGING ITENS
"""
list = ["horse", "monkey", "dog", "shark", "dragon", "phoenix"];
print(list);

print(type(list));
print(list[2]);

list[1] = 'cat';
print(list);

list[1:4] = ['bat', 'elephant', 'octopus'];
print(list);

# clue 1
list[1:2] = ['eagle', 'wolverine'];
print(list);
# added a element

print(list[1]);
print(list[2]);
print(list[3]);

# clue 2
list[1:5] = ['shark'];
print(list);
print(len(list));
# subtrack elements
"""

# ADDING ELEMENTS
"""
# index     0   1   2
list1 = ["car", "boat", "plane"];
print(list1);

for x in range(len(list1)):
    print(x, list[x]);

text = "car, plane";
list2 = list(text);
print(list2);

text = text.split(',');
print(text);

# good to split email names

list3 = ["car", "boat", "plane"];
print(list3);

# adding element to the end of the list

list3.append('motorcycle');
print(list3);
print(len(list3));

for x in range(len(list3)):
    print(x, list[x]);

# adding more than 1 element with append(list inside of a list)

list3.append(['bicycle', 'tricycle']);
print(list3);
print(len(list3));

# inserting elements in a chosen place

list3.insert(1, 'monocycle');
print(list3);
print(len(list3));

# adding more than 1 element (separated)

list3.extend('bicycle', 'tricycle');
print(list3);
print(len(list3));
"""

# REMOVE AND ORDENATE
"""
list = ["car", "boat", "plane", "motorcycle"];

# remove the last element of the list
list.pop();

# remove the specified element by me
list.remove("car");     # using element
list.pop(1);            # using index
del list[0];            # delet element using index
del list;               # delet list

bucket = ["product1", "product2", "product3"];
print(bucket);
for x in range(len(bucket)):
    print(bucket[x]);

bucket.clear();         # clear the elements in the vector;

bucket = ["bread", "meat", "product3"];
bucket.sort();

list2 = [1,50, 34, 68, 100];
list2.sort();           # ordenate to smaller to the greater;
print(list);

list2.sort(reverse = True);             # ordenate to greater to the smaller;
print(list2);

list2.reverse();        # reverse the elements of the list;
print(list2);

list3 = ["Ana", "Pedro", "Marta", "Larissa", "beatriz", "ana clara"];
print(list3);

list3.sort(key = str.lower);    # key to the sort
print(list3);
"""

# COPYING LISTS
"""
listA = ["a", "b", "c"];
listB = [1, 4, 6];

listA += listB;                  # listA + listB
print(listA);

# listA.extend(listB);             # listA + listB
# print(listA);

# for x in listB:                  # listA + listB
#     listA.append(x);
# print(listA);

listC = listB;
print(listC);

listC.append("d");
listB.append("e");

print(listC);
print(listB);

listD = listC.copy();
print(listD);

listD.append("f");
listC.append("g");
print(listC);
print(listD);
"""

# TUPLES
"""
list1 = ["element1", "element2", "element3"];
print(list1);
print(len(list1));
print(type(list1));
# list == mutable;

print("----"*10);

tuple1 = ("element1", "element2", "element3");
print(tuple1);
print(len(tuple1));
print(type(tuple1));
print(tuple1[2]);
# tuple == immutable;

tuple2 = ("element1", "element2", "element3", "element3", "element3");
print(tuple2);
print(len(tuple2));
print(type(tuple2));
print(tuple2[2]);
print(tuple2.count("element3"));

# isn't possible to add or subtrack a tuple,
# but it's possible to rewrite it with new values.

tuple2 = ("item3", "item4", "blue");
print(tuple2);

# MORE ABOUT TUPLES

# use examples
fed_units = ("CE", "DF", "GO", "RJ", "SP");
print(fed_units);
print(type(fed_units));

months = ("jan", "feb", "mar");
print(months);
print(type(months));

tuple3 = (3, 5.0, True, "item");

tuple4 = ("item2", );   #tuple is defined by commas, not by parentheses
print(tuple4);
print(type(tuple4));

tuple5 = ("item1", "item2", "item3", "item4");
list2 = list(tuple5);
print(tuple5);
print(list2);

list2.append("item5");
print(list2);

list2.pop();
print(list2);

tuple5 = tuple(list2);
print(tuple5);

# del tuple5; #error, because tuple5 isn't defined anymore

print(tuple5);
"""

# LOOPS WITH TUPLES
"""
tuple1 = ("item1",);
tuple2 = ("a", "b");

tuple1 = tuple1 + tuple1 + tuple2;
print(tuple1);
tuple2 = tuple2 * 3;
print(tuple2);

for variable in tuple1:
    print(variable);

for variable in range(len(tuple1)):
    print(variable, tuple1[variable]);
"""
# TUPLE UNPACKING

tupleA = ("item1", "item2", "item3");
print(tupleA)

(x, y, z) = tupleA;
print("x:", x);
print("y:", y);
print("z:", z);

tupleB = ("item1", "item2", "item3", "item4", "item5");
(x1, *y1, z1) = tupleB;
print("x1:", x1);
print("y1:", y1);
print("z1:", z1);
