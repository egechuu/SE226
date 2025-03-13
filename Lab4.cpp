//
// Created by ege on 13.03.2025.
//
#include <iostream>
using namespace std;

class Node {
public:
    int data;
    Node* next;
};

class Stack {
private:
    Node* head;     // Points to top element of stack.
    int num;        // Number of elements (index-style tracking).
    int capacity;   // Fixed size limit (resized when full).

public:
    Stack(int initialCapacity) {  // You can set any initial size.
        head = nullptr;
        num = -1;
        capacity = initialCapacity;
    }
    void push(int x) {
        if(capacity == num) {
          increaseCapacity();
        }
        if (head == nullptr) {
            head = new Node();
            head->data = x;
        }else {
            Node* newNode = new Node();
            newNode->data = x;
            newNode->next = head;
            head = newNode;
        }
        num++;
        cout<<"Pushed to the stack: "<<x<<endl;
    }

    int pop() {
        if(head == nullptr) {
          cout<<"Stack is empty. Can't pop."<<endl;
          return -1;
        }else {
          Node* newNode = head;
          head = head->next;
            int x = newNode->data;
          delete newNode;
          num--;
            cout<<"Popped from the stack: "<<x<<endl;
          return x;
        }
    }
    int peek() {
        if(head == nullptr) {
          cout<<"The stack is empty."<<endl;
          return -1;
        }
        cout<<"Top of the stack: "<<head->data<<endl;
        return head->data;
    }

    bool isEmpty() {
        return num < 0;
    }

    void increaseCapacity() {
        if(num == capacity) {
          cout<<"Increasing the capacity of the stack."<<endl;
          capacity *= 2;
        }
    }

    bool deleteElement(int val) {
        Node* temp1 = head;
        Node* temp2 = head;
        while(temp2 != nullptr && temp2->data != val) {
            temp1 = temp2;
            temp2 = temp2->next;
        }
        if(temp2 == nullptr) {
          cout<<"Element not found."<<endl;
          return false;
        }else {
          temp1->next = temp2->next;
          cout<<"Element deleted successfully."<<temp2->data<<endl;
          delete temp2;
          return true;
        }
    }
};

int main() {
    Stack s = Stack(1);
    s.push(10);
    s.push(20);
    s.push(30);
    s.push(40);
    s.peek();
    s.pop();
    s.deleteElement(10);
    s.pop();
    s.pop();
    s.pop();
    return 0;
}
