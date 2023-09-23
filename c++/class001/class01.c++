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

// CLASSES WITH A LOT OF METHODS

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
