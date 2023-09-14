"""
DO WHILE
"""
"""
# Guess the number

guess = 0
number = 9


#   {
while True:
    print("What is the correct number?")
    guess = int(input())
#   }DO WITHOUT VERIFYING
#   {
    if guess == number:
        print("Congratulations, you won.")
        break
    else:
        print("You lost")
#   }VERIFY
#   {
else:
    print("Error in app.")
    print(bol(guess))
#   }USEFUL WHILE DEVELOPING
"""

"""
# PAIR NUMBER

# How to know it

first = 5
second = 2

print(first%second)

# 0, 2, 4, 6, 8, ... PAIR
# 0/2, 2/2, 4/2, ... (1, 0)
"""
"""
print(20*"-")
number = int(input("Type a number to know if it's pair! "))

if (number % 2) == 0:
    print(f"{number} is pair")
else:
    print(f"{number} is impair")

print(20*"-")
"""

# FACTORIAL
"""
# 4! = 4*3*2*1
# 9! = 9*8*7*6*5*4*3*2*1
# 0! = 1
# 1! = 1

# 3! = 3*2*1 = 1*2*3

# Example 1

factorial = 1
number = int(input("Type the number to know the factorial: "))

if number < 0:
    print("Doesn't exist negative numbers factorial!")
elif number == 0:
    print(f"{number}! = {factorial}")
else:
    for x in range(1, number + 1):
        factorial *= x
    print(f"{number}! = {factorial}")
"""

# PRIME NUMBER
"""
# 7/1 = 7; Remainder = 0;
# 7/7 = 1; Remainder = 0;

print(40 * "-")

number = int(input("Type a number to know if it's a prime number: "))

if number > 1:
    for x in range(2, number):
        if (number % x) == 0:
            print(f"{number} is not a prime number")
            break
    else:
        print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number. Number less than or egual to 1")

print(40 * "-")
"""


# CONTINUE
"""
for x in range(10):
    if x == 3:
        continue
    # jump to the next repeating loop.
    print(x)
"""


# PASS
"""
if x == 5:
    pass
    # ignore the identation error. Careful using it.

print("Hello world")
"""

# ASSIGNMENT

# sites to train logics and compete online:

# urionlinejudge.com.br - URI
# hackerrank.com - hacker rank
# codechef.com - code chef
# codeingame.com - code game

"""
x = 0
print(f"1st x value: {x}")
x = 1
print(f"2nd x value: {x}")
x = x + 1
print(f"3rd x value: {x}")
x -= 1
print(f"4rd x value: {x}")
x *= 3
print(f"5nd x value: {x}")
x **= 3
print(f"6nd x value: {x}")
x = x % 3
print(f"7nd x value: {x}")
x = x / 3
print(f"8nd x value: {x}")
x = x // 5
"""
"""
#       0123456
name = "chicago"

print(name[0])


for x in range(1, 10, 1):
    print(x)

for x in range(10, 0, -1):
    print(x)


name1 = "chicago"
name2 = "queens"

print(name1, end=" ")
print(name2)

name3 = "chicago"

for x in name3:
    print(x, end="")

# python
x1 = 5
y1 = 2

x1, y1 = y1, x1

print(x1)
print(y1)
"""

# LISTS
"""
list = ["chicago", "queens", "brooklyn", "los angeles"]

list1 = [2, 3, 5, 6, 9]

list2 = [2.0, 3.0, 4.0, 5.0]

list3 = [True, False]

# index     0,  1,         2,  3 -> 4 elements;
list4 = [True, "chicago", 2.5, 4, False]

print(list)
print(list1)
print(list2)
print(list3)
print(list4)

print(list2[1])
print(type(list4))
print(list2[-1])
"""

# SLICING - numpy
"""
list1 = [2, 3, 5, 6, 9]
print(list1[::])  # return all index
print(list1[1:])  # return from index to the end of the list;
print(list1[:4])  # return from the beginning of list to index -1;
print(list1[1:3])  # return from first index to second index - 1;
print(list1[1:4:2])  # return from 1 to plus 2;

name = "earth"
print(name[2:4])  # slicing works with strings too;
"""

# FUNCTIONS
"""
list1 = [1, 3, 5]
list2 = [2.5, 3.6, 4.0]
# index =   0,      1,      2;
list3 = ["Name", "Name2", "Name"]

print(list1 + list2)
print(len(list1))  # length of the list;

# Functions that only can used with numerical data;

print(sum(list1))  # sum of all elements => x = 1 + 3 + 5;

print(max(list2))  # largest value of the list;

print(min(list1))  # smallest value of the list;
"""

# LIST FUNCTIONS
"""
name = "Python course"
value = range(10)

print(name)
print(value)

list10 = list(range(10))
print(list10)

list11 = list(name)
print(list11)

element = 8
if element in list10:
    print("Element inside the list.")
"""


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
