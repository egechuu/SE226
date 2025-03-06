//
// Created by ege on 4.03.2025.
//
#include <new>
#include <iostream>
using namespace std;

class Lab3 {
public:
	int data;
	Lab3 *next;

	Lab3(int x, Lab3 *n) {
		data = x;
		next = n;
	}
};

class Queue {
public:
	Lab3 *front;
	Lab3 *rear;
	int count;

	Queue() {
		front = nullptr;
		rear = nullptr;
		count = 0;
	}

	void enqueue(int x) {
		Lab3 *newNode = new Lab3(x, nullptr);
		if (front == nullptr) {
			front = newNode;
			rear = newNode;
		} else {
			rear->next = newNode;
			rear = newNode;
		}
		count++;
	}

	void dequeue() {
		Lab3 *temp = front;
		if (front == nullptr) {
			cout << "Queue is empty" << endl;
		} else {
			front = front->next;
			delete temp;
		}
		count--;
	}

	void printQueue() {
		Lab3 *temp = front;
		while (temp != nullptr) {
			cout << temp->data << endl;
			temp = temp->next;
		}
	}

	Lab3 *top() {
		if (!isEmpty()) {
			cout << front->data << endl;
			return front;
		}
		return nullptr;
	}

	bool isEmpty() {
		if (front == nullptr) {
			cout << "Queue is empty" << endl;
			return true;
		}
		cout << "Queue has elements." << endl;
		return false;
	}

	int size() {
		cout << "The queue has a size of: " << count << endl;
		return count;
	}
};

/*enqueue(int) : Adds an item in the queue.
- dequeue( ) : Removes an item from the queue.
- top( ) : Returns the top element of the queue.
- isEmpty( ) : Returns true if the queue is empty, else false.
- size( ) : Returns number of elements in the structure. This function is not shown in the
slides. It is your extra task to discover its implementation :)
 */


int main() {
	Queue *q = new Queue();
	q->enqueue(1);
	q->enqueue(2);
	q->enqueue(3);
	q->enqueue(4);
	q->enqueue(5);
	q->dequeue();
	q->printQueue();
	q->top();
	q->isEmpty();
	q->size();
	delete q;
	return 0;
}

