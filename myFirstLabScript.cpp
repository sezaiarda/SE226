#include <iostream>
#include <string>

using namespace std;

void q1() {
    string name;
    cout << "What is your name?\n";
    cin >> name;
    cout << "Hello " << name << ".\n";

    string student_id;
    cout << "What is your Student ID?\n";
    cin >> student_id;
    cout << "Your ID is " << student_id << "\n";
}

void q2() {
    double var1, var2;
    cout << "Enter var1\n";
    cin >> var1;
    cout << "Enter var2\n";
    cin >> var2;

    double var_sum = var1 + var2;
    double var_diff = var1 - var2;
    double var_prod = var1 * var2;

    cout << "var1: " << var1 << "\n"
         << "var2: " << var2 << "\n"
         << "sum: " << var_sum << "\n"
         << "diff: " << var_diff << "\n"
         << "prod: " << var_prod << "\n";
}

void q3() {
    string name;
    double lab, midterm, final;

    cout << "What is your name?\n";
    cin >> name;
    cout << "What is your lab grade?\n";
    cin >> lab;
    cout << "What is your midterm grade?\n";
    cin >> midterm;
    cout << "What is your final grade?\n";
    cin >> final;

    double last_score = lab * 0.25 + midterm * 0.35 + final * 0.4;
    cout << "Name: " << name << "\n"
         << "Lab: " << lab << "\n"
         << "Midterm: " << midterm << "\n"
         << "Final: " << final << "\n"
         << "Last Score: " << last_score << "\n";
}

void q4() {
    cout << "*\n**\n***\n**\n*\n";
}

int main() {
    q1();
    q2();
    q3();
    q4();
    return 0;
}
