#include<iostream>
#include<cstdlib>
using namespace std;

class UnderflowException{};

template<typename T>
class ListNode {
public:
	T value;
	ListNode<T>* next;
	ListNode<T>():next(nullptr){}
	ListNode<T>(T value1, ListNode<T>* next1):value(value1),next(next1){}
};

template<typename T>
class Stack {
public:
	int size;
	ListNode<T>* head;
	Stack<T>() : size(0), head(nullptr) {}

	~Stack<T>() {
		ListNode<T>* t1 = head, * t2;
		while (t1 != nullptr) {
			t2 = t1->next;
			delete t1;
			t1 = t2;
		}
	}
	void push(T value) {
		if (size == 0)head = new ListNode<T>(value, nullptr);
		else {
			ListNode<T>* t1 = new ListNode<T>(value, nullptr);
			t1->next = head;
			head = t1;
		}
		size++;
	}
	T front() {
		try {
			if (size == 0)throw UnderflowException();
			return head->value;
		}
		catch (UnderflowException e) {
			cerr << "Nothing in Stack.(Front)" << endl;
			exit(1);
		}
	}
	void pop() {
		try {
			if (size == 0)throw UnderflowException();
			ListNode<T>* temp = head;
			head = head->next;
			delete temp;
			size--;
		}
		catch (UnderflowException e) {
			cerr << "Nothing in Stack.(Pop)" << endl;
			exit(2);
		}
	}
};

template<typename T>
ostream& operator <<(ostream& out, const Stack<T>& LL) {
	ListNode<T>* temp = LL.head;
	out << "front [";
	for (int i = 0; i < LL.size; i++) {
		out << temp->value;
		temp = temp->next;
		if (i < LL.size - 1)out<<", ";
	}
	out << "] rear";
	return out;
}
int main() {
	Stack<int> S;
	S.push(0); cout << S << endl;
	S.push(1); cout << S << endl;
	S.push(2); cout << S << endl;
	S.pop(); cout << S << endl;
	S.push(4); cout << S << endl;
	S.pop(); cout << S << endl;
	S.pop(); cout << S << endl;
	S.push(5); cout << S << endl;
	S.pop(); cout << S << endl;
	S.pop(); cout << S << endl;
	S.pop(); cout << S << endl;
}