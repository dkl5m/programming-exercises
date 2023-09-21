#include <iostream>
using namespace std;

// CLASS AND OBJECTS

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