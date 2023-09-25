// HERITAGE

#include <iostream>
using namespace std;

// Exercise 1
// Make a program with a father class, cell child class,
// with its methods, and print everithing

/*
//Class Father
class Electronics{
    private:
        string brand;
    public:
        string getBrand(){
            return brand;
        }
        void setBrand(string brand){
            this->brand = brand;
        }
    protected:
        void isElectronic(){
            printf("\nIs electronic!\n");
        }
};

//Class Cell
class Cell: public Electronics{
    private:
        int inchs;
    public:
        Cell(){
            isElectronic();
        }
        int getInchs(){
            return inchs;
        }
        void setInchs(int inchs){
            this->inchs = inchs;
        }
};

int main(){
    Electronics electronic1;
    electronic1.setBrand("Motorola");
    cout << "Electronic1 Brand: " << electronic1.getBrand();

    Cell cell1;
    cell1.setBrand("Iphone");
    cell1.setInchs(5);
    cout << "Cell brand: " << cell1.getBrand() << "\n";
    cout << "Cell inchs: " << cell1.getInchs() << "\n";
    
    return 0;
}
*/

// OVERLOAD

// Exercise 1
// Make a program using overload in a function, and then,
// print it

/*
class Printer{
    public:
        void print(float cash){
            cout << "$: " << cash << endl;
        }
        void print(string phrase){
            cout << "-" << phrase << endl;
        }
};

int main(){
    // Will call each print function based on the type
    // and order of the called parameters
    Printer printer1;
    printer1.print("Hi guys!");
    printer1.print(25.8);

    return 0;
}
*/

// POLYMORPHISM

// Exercise 1
// Make a program using polymorphism in a function, and then,
// print it

/*
class Animal{
    public:
        void makeSound(){}
};

class Dog: public Animal{
    public:
        void makeSound(){
            cout << "Au au\n";
        }
};

class Cat: public Animal{
    public:
        void makeSound(){
            cout << "Miau miau\n";
        }
};

int main(){
    Dog dog1;
    dog1.makeSound();

    Cat cat1;
    cat1.makeSound();

    return 0;
}
*/

// ABSTRACT CLASS

class Geometrics{
    public:
        virtual int area() = 0;

        void setWidth(int width){
            this-> width = width;
        }

        void setHeight(int height){
            this-> height = height;
        }
    protected:
    int height;
    int width;
};

class Rectangle: public Geometrics{
    public:
        int Area(){
            return (width + height);
        }
};

class Triangle: public Geometrics{
    public:
        int Area(){
            return ((width + height)/2);
        }
};

int main(){
    Rectangle R;
    Triangle T;

    R.setInchs(5);
    R.setHeight(10);

    T.setInchs(5);
    T.setHeight(10);

    cout << "T area" << T.Area() << endl;
    cout << "R area" << R.Area() << endl;

    return 0;
}