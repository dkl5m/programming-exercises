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
// Extending the electronics class, give us access to all its
// public methods and attributes
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
    // can't use the protected methods with cell object in main
    // because those methods are presents just in the child class

    Cell cell1;
    cell1.setBrand("Iphone");
    cell1.setInchs(5);
    cout << "Cell brand: " << cell1.getBrand() << "\n";
    cout << "Cell inchs: " << cell1.getInchs() << "\n";
    
    return 0;
}
*/

// Exercise 2
// Make a program with an animal class with terrain, its getters and setters.
// Then, a mammal class, daughter of an animal with monthsGestation,
// its getters and setters.
// Then, a dog class that is the daughter of a mammal with breed, its getters
// and setters and a method for barking.
// Then create a dog with terrain, pregnancy month, breed and make it bark.

/*
class Animal{
    private:
        string terrain;
    public:
        string getTerrain(){
            return terrain;
        }
        void setTerrain(string newTerrain){
            terrain = newTerrain;
        }
};

class Mammal: public Animal{
    private:
        int monthsGestation;
    public:
        int getMonthsGestation(){
            return monthsGestation;
        }
        void setMonthsGestation(int newMonthsGestation){
            monthsGestation = newMonthsGestation;
        }
};

class Dog: public Mammal{
    private:
        string breed;
    public:
        string getBreed(){
            return breed;
        }
        void setBreed(string newBreed){
            breed = newBreed;
        }
        void bark(){
            cout << "Dog barks: Au au\n";
        }
};

int main(){
    Dog dog1;
    dog1.setTerrain("Grass");
    dog1.setMonthsGestation(4);
    dog1.setBreed("Dalmata");
    
    cout << "Dog1's terrain: " << dog1.getTerrain() << "\n" << endl;
    cout << "Dog1's gestation months: " << dog1.getMonthsGestation() << " months\n" << endl;
    cout << "Dog1's breed: " << dog1.getBreed() << "\n" << endl;
    dog1.bark();

    return 0;
}
*/

/*
// Exercise 2
// Make a program with an User class with name, email, and its getters and setters.
// Then, a Character class, daughter of User with increaseOneLevel method,
// its getters and setters.
// Then create a char with all methods.

class User{
    private:
        string name;
        string email;
    public:
        string getName(){
            return name;
        }
        void setName(string name){
            this->name = name;
        }
        string getEmail(){
            return email;
        }
        void setEmail(string email){
            this->email = email;
        }

};

class Character: public User{
    private:
        int level;
    public:
        int getLevel(){
            return level;
        }
        void setLevel(int level){
            this->level = level;
        }
        void increaseOneLevel(){
            this->level++;
        }
};

int main(){
    Character char1;
    char1.setName("King");
    char1.setEmail("contactking@king.com");
    char1.setLevel(3);
    
    cout<< "Name:" << char1.getName() << endl;
    cout<< "Email:" << char1.getEmail() << endl;
    cout<< "Level:" << char1.getLevel() << endl;
    
    char1.increaseOneLevel();
    cout<< "Increased Level:" << char1.getLevel() << endl;
    
    return 0;
}
*/

// Exercise 3
// Write a program with a person class with name and cpf, its getters and setters.
// Then a teacher class subclass of person with salary, its getters and setters.
// The teacher class must have two constructor methods, one that does not receive
// parameters and one that receives name, cpf and salary.
// Then, create a person with name and CPF and create an employee with name, CPF
// and salary.

/*
class Person{
    private:
        string name;
        string cpf;
    public:
        string getName(){
            return name;
        }
        void setName(string name){
            this->name = name;
        }
        string getCpf(){
            return cpf;
        }
        void setCpf(string cpf){
            this->cpf = cpf;
        }
};

class Teacher: public Person{
    private:
        float salary;
    public:
        float getSalary(){
            return salary;
        }
        void setSalary(float salary){
            this->salary = salary;
        }

        Teacher(){}

        Teacher(string name, string cpf, float salary){
            setName(name);
            setCpf(cpf);
            setSalary(salary);
        }

};

int main(){
    Person person1;
    person1.setName("Kaos");
    person1.setCpf("999.999.999-99");
    cout << "Person: " << person1.getName() << "-";
    cout << person1.getCpf() << "\n";

    Teacher functionary1("King", "666.666.666-66", 15000);
    cout << "Professor: " << functionary1.getName() << " - ";
    cout << functionary1.getCpf() << " - ";
    cout << functionary1.getSalary() << "\n";
 
    Teacher functionary2;
    functionary2.setName("Queen");
    functionary2.setCpf("888.888.888-88");
    functionary2.setSalary(15000);
    cout << "Professor: " << functionary2.getName() << " - ";
    cout << functionary2.getCpf() << " - ";
    cout << functionary2.getSalary() << "\n";

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

// Exercise 2
// Make a program with a calculator with two methods for adding,
// one of them receives 2 integers and the other receives 3 integers.
// The add method receives the parameters and returns their sum.
// Test the calculator by adding and displaying 2 values and then
// 3 values on the screen.

/*
class Sum{
    public:
        void sum(int num1, int num2){
            cout << num1 << " + " << num2 << " = " << num1+num2 <<endl;
        }
        void sum(int num1, int num2, int num3){
            cout << num1 << " + " << num2 << " + " << num3 << " = " << num1+num2+num3 <<endl;
        }
};

int main(){
    Sum sum1;
    sum1.sum(4,5);
    sum1.sum(4,5,6);

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
        // virtual method (empty)
        void makeSound(){}
};

class Dog: public Animal{
    public:
        // calling makeSound() in dog will call this method
        void makeSound(){
            cout << "Au au\n";
        }
};

class Cat: public Animal{
    public:
        // calling makeSound() in cat will call this method
        void makeSound(){
            cout << "Miau miau\n";
        }
};

int main(){
    Dog dog1;
    // this method overlap the Animal one
    dog1.makeSound();

    Cat cat1;
    cat1.makeSound();

    return 0;
}
*/

// Exercise 2
// Make a program with a language class and a greeting method,
// then create 3 subclasses using polymorphism to print the
// greeting on the screen in each different language according
// to the name of the subclass.

/*
class Language{
    public:
        void greeting(){};
};

class English: public Language{
    public:
        void greeting(){
            cout << "English Greeting: Hello!\n";
        }
};

class Portuguese: public Language{
    public:
        void greeting(){
            cout << "Portuguese Greeting: Oi!\n";
        }
};

class Spanish: public Language{
    public:
        void greeting(){
            cout << "Spanish Greeting: Ola!\n";
        }
};

int main(){
    English english1;
    english1.greeting();

    Portuguese portuguese1;
    portuguese1.greeting();

    Spanish spanish1;
    spanish1.greeting();

    return 0;
}
*/

// Exercise 3
// Write a program with a menu class with a showoptions()
// method and two child classes menucliente and
// menuadministrator showing different system access options.

class Menu{
    public:
        void showOptions(){};
};

class ClientMenu{
    public:
        void showOptions(){
            cout << "Client Menu" <<endl;
            cout << "1 - Buy" <<endl;
            cout << "2 - Sell" <<endl;
            cout << "3 - Exit\n" <<endl;
        }
};

class AdministratorMenu{
    public:
        void showOptions(){
            cout << "Administrator Menu" <<endl;
            cout << "1 - Buy" <<endl;
            cout << "2 - Sell" <<endl;
            cout << "3 - Register new product" <<endl;
            cout << "4 - Erase product" <<endl;
            cout << "5 - Exit" <<endl;    
        }
};

int main(){
    ClientMenu menu1;
    menu1.showOptions();

    AdministratorMenu menu2;
    menu2.showOptions();

    return 0;
}

// ABSTRACT CLASS
/*
class Geometrics{
    public:
        //virtual function will be overlaped
        virtual int Area() = 0;

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

//Rectangle is a geometric form
class Rectangle: public Geometrics{
    public:
        //overwrite Geometrics Area()
        int Area(){
            return (width * height);
        }
};

//Triangle is a geometric form
class Triangle: public Geometrics{
    public:
        //overwrite Geometrics Area()
        int Area(){
            return ((width * height)/2);
        }
};

int main(){
    Rectangle R;
    Triangle T;

    R.setWidth(5);
    R.setHeight(10);

    T.setWidth(5);
    T.setHeight(10);

    cout << "T area: " << T.Area() << " units^2" << endl;
    cout << "R area: " << R.Area() << " units^2" << endl;

    return 0;
}
*/