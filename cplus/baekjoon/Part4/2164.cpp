#include<iostream>
#include<cstdlib>
using namespace std;

template<typename T>
class ListNode {
public:
	T value;
	ListNode<T>* next;
	ListNode<T>() : next(nullptr) {}
	ListNode<T>(T value1, ListNode<T>* next1) : value(value1), next(next1) {}
};

template<typename T>
class Queue {
public:
	int size;
	ListNode<T>* head;
	ListNode<T>* tail;
	Queue<T>() : size(0), head(nullptr), tail(nullptr) {}

	~Queue<T>() {
		ListNode<T>* t1 = head, * t2;
		while (t1 != nullptr) {
			t2 = t1->next;
			delete t1;
			t1 = t2;
		}
	}
	void push(T value) {
		if (size == 0) { head = new ListNode<T>(value, nullptr); tail = head; }
		else {
			ListNode<T>* t1 = new ListNode<T>(value, nullptr);
			tail->next = t1;
			tail = t1;
		}
		size++;
	}
	T front() {
		if (size == 0) return -1;
		else {
			return head->value;
		}
	}
	T back() {
		if (size == 0)return -1;
		else {
			return tail->value;
		}
	}
	T pop() {
		if (size == 0) return -1;
		else {
			ListNode<T>* temp = head;
			T tmp = head->value;
			head = head->next;
			delete temp;
			size--;
			return tmp;
		}
	}
	bool empty() {
		if (size == 0)return true;
		else return false;
	}
};

int main() {
	int N;
	scanf("%d", &N);
	int i = 1;
	if (N == 1) { puts("1"); return 0; }
	Queue<int> Q;
	while (i <= N) {
		Q.push(i++);
	}
	while (true) {
		Q.pop();
		if (Q.size == 1) { printf("%d", Q.pop()); break; }
		Q.push(Q.pop());
	}
	return 0;
}
