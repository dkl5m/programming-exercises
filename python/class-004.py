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