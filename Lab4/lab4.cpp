#include <iostream>
#include <string>
#include <sstream>
using namespace std;

class Node {
public:
    int data;
    Node* next;
};

class Stack {
private:
    Node* head;
    int num;
    int capacity;

public:
    Stack(int initialCapacity) {
        head = nullptr;
        num = -1;
        capacity = initialCapacity;
    }

    void push(int x) {
        if (num + 1 >= capacity) {
            increaseCapacity();
        }

        Node* newNode = new Node();
        newNode->data = x;
        newNode->next = head;
        head = newNode;
        num++;
    }

    int pop() {
        if (isEmpty()) {
            cout << "Stack underflow" << endl;
            return -1;
        }

        int value = head->data;
        Node* temp = head;
        head = head->next;
        delete temp;
        num--;
        return value;
    }

    int peek() {
        if (isEmpty()) {
            cout << "Stack is empty" << endl;
            return -1;
        }

        return head->data;
    }

    bool isEmpty() {
        return num < 0;
    }

    void increaseCapacity() {
        capacity *= 2;
        cout << "Capacity increased to " << capacity << endl;
    }

    bool deleteElement(int val) {
        if (isEmpty()) {
            return false;
        }

        if (head->data == val) {
            Node* temp = head;
            head = head->next;
            delete temp;
            num--;
            return true;
        }

        Node* current = head;
        while (current->next != nullptr && current->next->data != val) {
            current = current->next;
        }

        if (current->next != nullptr) {
            Node* temp = current->next;
            current->next = current->next->next;
            delete temp;
            num--;
            return true;
        }

        return false;
    }

    string toString() const {
        stringstream ss;
        ss << "[";
        Node* current = head;
        while (current != nullptr) {
            ss << current->data;
            if (current->next != nullptr) {
                ss << ", ";
            }
            current = current->next;
        }
        ss << "]";
        return ss.str();
    }
};

int main() {
    // Test cases
    Stack s(2);
    cout << "Initial stack: " << s.toString() << endl;

    s.push(1);
    cout << "Stack after pushing 1: " << s.toString() << endl;

    s.push(2);
    cout << "Stack after pushing 2: " << s.toString() << endl;

    s.push(3);
    cout << "Stack after pushing 3: " << s.toString() << endl;

    cout << "Popped element: " << s.pop() << endl;
    cout << "Stack after popping: " << s.toString() << endl;

    cout << "Peek: " << s.peek() << endl;

    cout << "Is empty? " << s.isEmpty() << endl;

    s.deleteElement(1);
    cout << "Stack after deleting 1: " << s.toString() << endl;

    s.deleteElement(2);
    cout << "Stack after deleting 2: " << s.toString() << endl;

    cout << "Is empty? " << s.isEmpty() << endl;

    return 0;
}