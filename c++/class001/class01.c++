#include <iostream>
using namespace std;

// CLASS AND OBJECTS

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

// READING CLASS VALUES

class Cookie {
    public:
        float price;
        string flavor;
};

int main(){
    Cookie cookie1;

    cout << "Type the cookie price: ";
    cin >> cookie1.price;

    cout << "Type the cookie flavor: ";
    cin. sync();

    getline(cin, cookie1.flavor );

    cout << "Cookie1:" << cookie1.flavor;
    cout << " costs $" << cookie1.price;


    return 0;
}