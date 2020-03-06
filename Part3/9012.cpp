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
		ListNode<T>* t1 = head;
		head = head->next;
		delete t1;
		size--;
	}
	int s() {
		return size;
	}
};

int main() {
	int N;
	cin >> N;
	for (int i = 0; i < N; i++) {
		Stack<char> S;
		getchar();
		char key[100] = { 0, };
		cin >> key;
		int j = 0;
		while (key[j]) {
			if (key[j] == '(')S.push(key[j++]);
			else {
				if (S.s() == 0) break;
				S.pop();
				j++;
			}
		}
		if (key[j]==0&&S.s() == 0)cout << "YES" << endl;
		else cout << "NO" << endl;
	}
	return 0;
}