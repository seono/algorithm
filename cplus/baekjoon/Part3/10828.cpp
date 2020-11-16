#include <iostream>
#include <cstdlib>
using namespace std;

class UnderflowException {};

template<typename T>
class ListNode {
public:
	T value;
	ListNode<T>* next;
	ListNode<T>() : next(nullptr) {}
	ListNode<T>(T value1, ListNode<T>* next1) : value(value1), next(next1) {}
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
	void pop() {
		try {
			if (size == 0)throw UnderflowException();
			cout << head->value << endl;
			ListNode<T>* t1 = head;
			head = head->next;
			delete t1;
			size--;
		}
		catch (UnderflowException e) {
			cout << "-1" << endl;
		}
	}
	void s() {
		cout << size << endl;
	}
	void empty() {
		if (size)cout << "0" << endl;
		else cout << "1" << endl;
	}
	void top() {
		try {
			if (size == 0)throw UnderflowException();
			cout << head->value << endl;
		}
		catch (UnderflowException e) {
			cout << "-1" << endl;
		}
	}
};

int main() {
	int N;
	Stack<int> S;
	cin >> N;
	for (int i = 0; i < N; i++) {
		getchar();
		char key[10] = { 0, };
		cin >> key;
		switch (key[0])
		{
		case 'p':if (key[1] == 'u') {
			int t;
			cin >> t;
			S.push(t);
		}
				else {
			S.pop();
		}
				break;
		case 't':S.top(); break;
		case 's':S.s(); break;
		case 'e':S.empty(); break;
		default:
			break;
		}
	}
	return 0;
}