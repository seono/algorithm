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
	bool large(T *arr) {
		ListNode<T>* temp = head;
		T tmp = head->value;
		while (temp != nullptr) {
			if (arr[temp->value] > arr[tmp])return false;
			temp = temp->next;
		}
		return true;
	}
	bool empty() {
		if (size == 0)return true;
		else return false;
	}
};

template<typename T>
ostream& operator <<(ostream& out, const Queue<T>& LL) {
	ListNode<T>* temp = LL.head;
	out << "front [";
	for (int i = 0; i < LL.size; i++) {
		out << temp->value;
		temp = temp->next;
		if (i < LL.size - 1)out << ", ";
	}
	out << "] rear";
	return out;
}

int main() {
	int N;
	scanf("%d", &N);
	while (N--) {
		Queue<int> Q;
		int n, m, ans = 0;
		scanf("%d %d", &n, &m);
		int* arr = new int[n];
		for (int i = 0; i < n; i++) {
			scanf("%d", &arr[i]); Q.push(i);
		}
		int worked = 1;
		while (true) {
			if (Q.large(arr)) {
				ans++;
				if (Q.pop() == m) {
					printf("%d\n", ans); break;
				}
			}
			else Q.push(Q.pop());
		}
	}
	return 0;
}