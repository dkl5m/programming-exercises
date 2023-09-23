#include <iostream>
using namespace std;

// CLASS AND OBJECTS

// Exercise 1
// Make a program that define a class, create a object
// and print it's attributes

/*
class Cookie{           // Defining class Cookie
    public:             // Acess modified
        float price;    // Price attribute
        string taste;   // Taste attribute
};

int main(){
    Cookie Cookie1;             // Create an object to the class
    Cookie1.price = 15.35;      // Change price of object
    Cookie1.taste = "Chocolate";// Change taste of object

    Cookie Cookie2;
    Cookie2.price = 20.00;
    Cookie2.taste = "Flakes";

    cout << "Cookie1:" << cookie1.taste;
    cout << " costs $" << cookie1.price << "\n";
    cout << "Cookie2:" << cookie2.taste;
    cout << " costs $" << cookie2.price << "\n";

    return 0;
}
*/

// CLEANING THE INPUT BUFFER

// Exercise 1
// Make a program that write a phrase, receive the
// phrase, clean the buffer and print the value received

#include <ios>
#include <limits>

/*
int main(){
    char phrase[80];

    cout << "Write a phrase: ";
    cin.sync();                 // Clean the buffer

    cin.getline(phrase, 80);
    cout << "\nPhrase:" << phrase <<"\n";

    return 0;
}
*/

// READING CLASS VALUES AND CREATING CLASS OBJECTS

// Exercise 1
// Make a program that define a class, create a object
// and print it's attributes, cleaning the buffer to show 
// strings

/*
class Cookie {          // defining the mold to Cookies
    public:             // access modifier
        float price;    // price attribute
        string flavor;  // flavor attribute
};

int main(){
    Cookie cookie1;     // create class object

    cout << "Insert the cookie price:";
    cin >> cookie1.price;
    cin.sync();         // clear the buffer

    cout << "Insert the cookie flavor: ";
    cin.ignore();       // discard the trailing '\n'
        // (better always use before getline command)

    getline(cin, cookie1.flavor);   // read the flavor
                                    // even with spaces

    cout << "\nCookie1:" << cookie1.flavor;
    cout << " costs $" << cookie1.price;
    cout << "\n";

    return 0;
}
*/

// CONSTRUCTORS

// Exercise 1
// Make a program that define a class, create a constructor,
// a object and print it's attributes

/* 
 class Cookie{
    public:
        float price;
        string flavor;
        string format;
    
    // Constructor method is initialized when
    // the class was created
    Cookie(){
        printf("Cookie created!\n");
        format = "round";
        // initiate format as round
    }
 };

 int main(){
    Cookie cookie1;
    cookie1.price = 15;
    cookie1.flavor = "chocolate";

    cout << "Cookie 1: " << cookie1.flavor;
    cout << " costs $ " << cookie1.price;
    cout << ", format " << cookie1.format;

    return 0;
 }
*/

// CONSTRUCTOR WITH PARAMETERS

// Exercise 2
// Make a program that define a class, create a constructor
// with parameters, a object and print it's attributes

/*
 class Person{
    public:
        string name;
        
    Person(){
        printf("Person created without name\n");
    }

    Person(string newName){
        printf("Person created with name\n");
        name = newName;
    }
 };

 int main(){
    // Create Person class object without name
    Person person1;
    cout << "Person1 " << person1.name << "\n";
    // Change the person name
    person1.name = "King";
    cout << "Person1 " << person1.name << "\n\n";

    // Create Person class object with name
    Person person2("Manta");
    cout << "Person2 " << person2.name << "\n";

    return 0;
 }
*/

// Exercise 3
// Make a program that define a class, create different
// constructors and objects and print it's attributes

/*
class Person{
    public:
        string name;
        int age;

    Person(){
        printf("Person created without name nor age");
    }

    Person(string newName){
        printf("Person created with name");
        name = newName;
    }

    Person(int newAge){
        printf("Person created with age");
        age = newAge;
    }

    Person(string newName, int newAge){
        printf("Person created with name and age");
        name = newName;
        age = newAge;
    }
};

int main(){

    Person person1;
    cout << "\nPerson1 " << person1.name << ", " << person1.age << "\n";

    Person person2("King ");
    cout << "\nPerson2 " << person2.name << ", " << person2.age << "\n";

    Person person3(25);
    cout << "\nPerson3 " << person3.name << ", " << person3.age << "\n";

    Person person4("Kang", 25);
    cout << "\nPerson4 " << person4.name << ", " << person4.age << "\n";

    return 0;
}
*/

// Exercise 4
// Write a program that reads a flavor entered by the user, then with a
// coxinha class, create the coxinha and assign the flavor entered using
// the constructor method with one parameter

/*
class Coxinha{
    public:
        string flavor;

    Coxinha(string newFlavor){
        printf("Coxinha created! \n");
        flavor = newFlavor;
    }
};

int main(){
    string flavor;
    
    cout << "Type the flavor you want: " << "\n ";
    cin >> flavor;

    Coxinha coxinha1(flavor);
    cout << "Coxinha 1 has the flavor of " << coxinha1.flavor << "!\n";
    
    return 0;
}
*/

// Exercise 5
// Make a program with a dog class that has a breed and it is possible to
// create a dog already informing the breed, or without informing it. If
// not informed, attribute the breed to a little mongrel

/*
class Dog{
    public:
        string breed;
    
    Dog(){
        printf("Dog created!\n");
        breed = "little mongrel";
    }

    Dog(string newBreed){
        printf("Dog created!\n");
        breed = newBreed;
    }
};

int main(){
    Dog dog1;
    cout << "The dog1 breed is " << dog1.breed << "\n";
    Dog dog2("Dobberman");
    cout << "The dog2 breed is " << dog2.breed << "\n";

    return 0;
}
*/

// CLASSES WITH A LOT OF METHODS

// Exercise 1
// Make a program that define a class with different
// methods, create a object and print it's attributes

/*
class Person{
    public:
        string name;

    Person(string newName){
        printf("Person created with name");
        name = newName;
    }

    // print a phrase on scream method
    void talk(string phrase){
        cout << name << " say: " << phrase;
    }

    // scream method
    void scream(){
        cout << " AHHHH ";
    }
};

int main(){

    Person person2(" King");
    person2.talk("What's up?");
    person2.scream();

    return 0;
}
*/

// Exercise 2
// Write a program with a person class that receives name, age
// and salary information directly when constructing the object
// and associates it with the correct fields.
// Add a method to print the fields

/*
class Person{
    public:
        string name;
        int age;
        float salary;

    Person(string newName, int newAge, float newSalary){
        name = newName;
        age = newAge;
        salary = newSalary;
    }

    void print(){
        cout << "The worker called " << name;
        cout << " is " << age << " years old ";
        cout << " and earns $" << salary << "per month!\n";
    }
};

int main(){
    string name;
    int age;
    float salary;

    cout << "Type the worker's name: \n";
    cin.sync();
    getline(cin, name);

    cout << "Type the worker's age: \n";
    cin.sync();
    cin >> age;

    cout << "Type the worker's salary: \n";
    cin.sync();
    cin >> salary;
    cout << "\n";

    Person person1(name, age, salary);
    person1.print();

    return 0;
}
*/

// Exercise 3
// Write a program with a calculator class that performs addition,
// subtraction, division and multiplication operations and test
// the methods with examples

/*
class Calculator{
    public:
        int result;

    Calculator(){
        printf("Calculator created!\n");
    }

    int sum(int x, int y){
        result = x + y;
        return result;
    }
    int subtraction(int x, int y){
        result = x - y;
        return result;
    }
    int division(int x, int y){
        result = x / y;
        return result;
    }
    int multiplication(int x, int y){
        result = x * y;
        return result;
    }
};

int main(){
    Calculator calculator1;
    cout << "Sum: " << calculator1.sum(10,5) << ".\n";
    cout << "Subtraction: " << calculator1.subtraction(10,4) << ".\n";
    cout << "Division: " << calculator1.division(10,4) << ".\n";
    cout << "Multiplication: " << calculator1.multiplication(10,4) << ".\n";
    return 0;
}
*/

// METHODS WITH RETURN

// Exercise 1
// Make a program that define a class with methods that
// return values, create a object and print it's attributes

/*
class Calculator{
    public:
        Calculator(){
            printf("Calculator created!\n");
        }

        int sum(int x, int y){
            int result = x + y;
            return result;
        }
};

int main(){
    Calculator myCalculator;
    cout << "x + y = " << myCalculator.sum(10,20) << "\n ";

    return 0;
}
*/

// GETTERS AND SETTERS

// Exercise 1
// Make a program that define a class with private and public
// methods that return values, create a object and print
// it's attributes

/*
// Defining the mold to persons
class Person{
    private:
        // Name attribute
        string name;
    
    // Access modifier
    public:
        // Name getter, return actual name
        string getName(){
            return name;
        }

        // Name setter, update name
        void setName(string newName){
            name = newName;
            //setName(newName);
        }
};

// Getters and Setters make your data more secure, because
// the program doesn'l allow you to change the classes vars
// without these methods.

int main(){
    // Create Person without attributes
    Person person1;
    // Modify the name
    person1.setName("King");
    // Print the name
    cout << person1.getName() << "\n";
    person1.setName("Kaos");
    // Print the name
    cout << person1.getName() << "\n";
    return 0;
}
*/

// Exercise 2
// Make a program with a cell class, with the attributes brand
// and price. Use encapsulation and add the respective GETTERS
// and SETTERS methods.

class Cell{
    private:
        string brand;
        int price;
    public:
        Cell(){
            brand = "";
            price = 0;
        }
        Cell(string brand){
            setBrand(brand);
        }
        Cell(int price){
            setPrice(price);
        }
        Cell(string brand, int price){
            setBrand(brand);
            setPrice(price);
        }


        string getBrand(){
            return brand;
        }
        void setBrand(string newBrand){
            brand = newBrand;
        }
        int getPrice(){
            return price;
        }
        void setPrice(int newPrice){
            price = newPrice;
        }
};

int main(){
    string brand;
    int price;

    Cell cell1;
    cout << "Cellphone brand: " << cell1.getBrand() << ".\n";
    cout << "Cellphone price: $" << cell1.getPrice() << ".\n\n";
    
    Cell cell2("Motorola");
    cout << "Cellphone brand: " << cell2.getBrand() << ".\n";
    cout << "Cellphone price: $" << cell2.getPrice() << ".\n\n";
    
    Cell cell3(1800);
    cout << "Cellphone brand: " << cell3.getBrand() << ".\n";
    cout << "Cellphone price: $" << cell3.getPrice() << ".\n\n";
    
    Cell cell4("Motorola", 1800);
    cout << "Cellphone brand: " << cell4.getBrand() << ".\n";
    cout << "Cellphone price: $" << cell4.getPrice() << ".\n";

    return 0;
}