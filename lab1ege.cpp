#include <iostream>
#include <cmath>
using namespace std;
int main() {
    //1
    string name;
    cout << "What is your name?";
    cin >> name;
    cout << "Hello " << name << "\n";

    int id;
    cout << "What is your Student ID? " << "\n";
    cin >> id;
    cout << "Your ID is " << id<<"\n";
    //2
    int var1;
    cout << "Enter first number. " << "\n";
    cin >> var1;

    int var2;
    cout << "Enter second number. " << "\n";
    cin >> var2;

    int sum = var1 + var2;
    int diff = int(abs(double(var1)-double(var2)));

    int prod = var1*var2;

    cout << "Sum: " << sum << "\n";
    cout << "Difference: " << diff << "\n";
    cout << "Product: " << prod << "\n";
    //3
    string fullname;
    cout << "Enter full name. " << "\n";
    cin >> fullname;

    float lab;
    cout << "Enter lab grade. " << "\n";
    cin >> lab;

    float midterm;
    cout << "Enter midterm grade. " << "\n";
    cin >> midterm;

    float finalGrade;
    cout << "Enter final grade. " << "\n";
    cin >> finalGrade;

    float lastScore = lab*0.25 + midterm*0.35 + finalGrade*0.4;
    cout << "Name: " << name << "\n";
    cout << "Lab: " << lab << "\n";
    cout << "Midterm: " << midterm << "\n";
    cout << "Final: " << finalGrade << "\n";
    cout << "Last Score: " << lastScore << "\n";

    //4
    cout << "*\n**\n***\n**\n*";
    return 0;

}
