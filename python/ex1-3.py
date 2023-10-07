"""
Python Exercise 01

Obs: All exercises must use input function, so that the user can determine the input data.

01 - retangle area;
02 - triangle area;
03 - square area;
04 - if the product that you want to evaluate costs (??), what will be it's value wiht a discount of (%%)?;
05 - circle area, with pi = 3,141592;
06 - reais to dolar conversion;
07 - dolar to reais conversion;
"""

"""
#1
print("----Retangle area calculator----");
value01 = input("Type the base value: ");
value02 = input("Type the height value: ");
area = (float(value01) * float(value02));
print(f"The area value is: {area} measure units!");

#2
print("----Triangle area calculator----");
value01 = float(input("Type the 1st value: "));
value02 = (input("Type the 2nd value: "));
area = (float(value01) * float(value02)) / 2;
print(f"The area value is: {area} measure units!");

#3
print("----Square area calculator----");
value01 = input("Type the value: ");
area = (float(value01))**2;
print(f"The area value is: {area} measure units!");

#4
print("----Final value calculator?----");
value01 = input("Type the base value: ");
value02 = input("Type the discount value, in percentage: (example: 10%) ");
# finalValue = baseValue - (baseValue*discount) = baseValue*(1-discount/100);
finalValue = float(value01)*(1 - float(value02)/100);
print(f"The final value is: {finalValue} money!");

#5
print("----Circle area calculator----");
pi = 3.141592;
radius = float(input("Type the radius value: "));
area = pi*(radius**2);
print("The area value is {area:.2f} measure units!");

#6
print("----Reais to dollars conversion calculator----");
real = float(input("Type the reals value: (example:5.92) "));
cotationValue = float(input("Type the dollars cotation: (example:1 dollar = 4.85 reals, type 4.85) "));
# 1 dollar = 4.85 reals, x dollars = 300 reals, x dollars = (300 * 1) / 4.85;
dollar = real / cotationValue;
print(f"The value is: U$ {dollar:.2f}. Cotation: {cotationValue:.2f}.");

#7
print("---- Dollars to reais conversion calculator----");
dollar = float(input("Type the dollars value: (example:5.92) "));
cotationValue = float(input("Type the dollars cotation: (example:1 dollar = 4.85 reals, type 4.85) "));
# 1 dollar = 4.85 reais, 300 dollars = x reais, x reals = 300 * 4.85;
real = dollar * cotationValue;
print(f"The value is: R$ {real:.2f}. Cotation: {cotationValue:.2f}.");
"""


"""
Python Exercise 02

01 - Implement a program that receives a person's age and prints a message from according to the criteria;
    Under 16 years old: MINOR
    Between 16 and 18 years old: EMANCIPATED
    Over 18 years old: MAJOR

02 - Implement a program that receives the age of a swimmer and prints his category following the rules:
    Category        Age
    childish A      5 - 7 years
    childish B      8 - 10 years
    juvenile A      11 - 13 years
    juvenile B      14 - 17 years
"""

"""
#1
age = int(input("Type your age: "));
if age < 16:
    print("MINOR");
elif 16 <= age <= 18:
    print("EMANCIPATED");
else:
    print("MAJOR");
"""

"""
#2
age = int(input("Type your age: "));
if age < 5: print("Not allowed");
elif 5 <= age <= 7: print("childish A");
elif 8 <= age <= 10: print("childish B");
elif 11 <= age <= 13: print("juvenile A");
elif 14 <= age <= 17: print("juvenile B");
else: print("not specified");
"""


"""
Python Exercise 03
All exercises have some repeating form logic that you can use
repeating loops to develop them.
01 - Write a program that reads 5 values ​​and finds the largest and smallest of them. show the
result.
    Analysis:
    I could assume that the smallest was any small number (or that the largest
    was a large number) instead of initially assuming it to be the first?
    Answer: No!
    
    Example: Suppose that the value -500 was assigned to the smallest variable and that the
    user entered only values ​​greater than -500 (example: -10, -9, 0, 6, 7 and 450),
    if the value stored in the smaller variable is never changed, the assumption would be
    incorrect - logic error - because the supposedly smaller value would be outside the set
    values ​​entered and therefore valid). The same reasoning applies to larger
    
    Solution: Assume that the major and minor variables assume the value of the first
    typed element, outside the repetition structure. Thus, in the case of the minor
    element, by comparing the value currently stored in this variable with the
    other typed elements (from the 2nd onwards) it can be changed (or not, if
    the smallest of all entered values ​​is effectively the first). Likewise,
    the value of the larger variable can be changed, if there is one between the numbers
    subsequently typed a value greater than the one considered the highest until then.

02 - Write a program to calculate the sums:
S = 3/40 + 32 /39 + 33 /38 + 34 /37 + 340/1
S = 480/2 + 475/22 + 470/23 + 465/24 + 460/25 + (first 20 terms)
S = 1/2 + 3/23 + 7/25 + 15/27 + 31/29 + (first 15 terms)
"""


"""
#1
smallestValue = largestValue = number = 0;

for x in range(5):
    if x == 0:
        #number = int(input("Type a number and press enter: "));
        smallestValue = largestValue = number = int(input("Type a number and press enter: "));
    elif x > 0:
        number = int(input("Type a number and press enter: 444"));
        if number > smallestValue:
            largestValue = number;
        elif number < smallestValue:
            smallestValue = number;
        else:
           number = smallestValue;
    print(f"smallest: {smallestValue}; largest: {largestValue}.");

"""

"""
# 2 - a)

sum = 3/40 + 32 /39 + 33 /38 + 34 /37 + 340/1;
print(f"A) Value = {sum}.");

# 2 - b)

numerator = 480;
denominator = 2;
sum = numerator / denominator;

for x in range(20):
    if x == 0:
        numerator = 480;
        denominator = 2;
        sum = numerator / denominator;
    elif x > 0:
        numerator = 480 - (x - 1) * 5;
        denominator = 21 + (x - 1) * 1;
        sum += numerator / denominator;
print(f"Sum value: {sum}.");

#2 c)

numerator = 1;

for x in range(15):
    if(x == 0):
        denominator = 2;
        sum = numerator / denominator;
    elif(x > 0):
        numerator = numerator + (2 ** (x - 1));
        denominator = 21 + 2 * (x - 1);
        sum += numerator / denominator;
print(f"Sum value: {sum}.");
"""
