#include<iostream>
#include<cstdlib>
using namespace std;

template <typename T>
class ListNode {
public:
	T value;
	ListNode<T>* next, * rear;
	ListNode<T>() : next(nullptr), rear(nullptr) {}
	ListNode<T>(T value1, ListNode<T>* next1, ListNode<T>* rear1) : value(value1), next(next1), rear(rear1) {}
};

template<typename T>
class Deque {
public:
	int size;
	ListNode<T>* head, * tail;
	Deque<T>() : size(0), head(nullptr), tail(nullptr) {}

	~Deque<T>() {
		ListNode<T>* t1 = tail, * t2;
		while (t1 != nullptr) {
			t2 = t1->next;
			delete t1;
			t1 = t2;
		}
	}
	void push_front(T value) {
		if (size == 0) {
			head = new ListNode<T>(NULL, nullptr, nullptr);
			tail = new ListNode<T>(NULL, nullptr, nullptr);
			ListNode<T>* t1 = new ListNode<T>(value, head, tail);
			head->rear = t1;
			tail->next = t1;
		}
		else {
			ListNode<T>* t1 = new ListNode<T>(value, head, nullptr);
			t1->rear = head->rear;
			head->rear->next = t1;
			head->rear = t1;
		}
		size++;
	}
	void push_back(T value) {
		if (size == 0) {
			head = new ListNode<T>(NULL, nullptr, nullptr);
			tail = new ListNode<T>(NULL, nullptr, nullptr);
			ListNode<T>* t1 = new ListNode<T>(value, head, tail);
			head->rear = t1;
			tail->next = t1;
		}
		else {
			ListNode<T>* t1 = new ListNode<T>(value, nullptr, tail);
			t1->next = tail->next;
			tail->next->rear = t1;
			tail->next = t1;
		}
		size++;
	}
	T pop_front() {
		if (size == 0)return -1;
		else {
			ListNode<T>* t1 = head->rear;
			T tmp = t1->value;
			head->rear = t1->rear;
			head->rear->next = head;
			delete t1;
			size--;
			return tmp;
		}
	}
	T pop_back() {
		if (size == 0)return -1;
		else {
			ListNode<T>* t1 = tail->next;
			T tmp = t1->value;
			tail->next = t1->next;
			t1->next->rear = tail;
			delete t1;
			size--;
			return tmp;
		}
	}
	bool empty() {
		if (size == 0)return true;
		else return false;
	}
	T front() {
		if (size == 0)return -1;
		else {
			T tmp = head->rear->value;
			return tmp;
		}
	}
	T back() {
		if (size == 0)return -1;
		else {
			T tmp = tail->next->value;
			return tmp;
		}
	}
};

int main() {
	int N;
	cin >> N;
	while (N--) {
		string order;
		cin >> order;
		int s;
		cin >> s;
		Deque<int> D;
		int tmp;
		getchar();
		getchar();
		if (s > 0) {
			scanf("%d", &tmp);
			D.push_back(tmp);
			for (int i = 1; i < s; i++) {
				scanf(",%d", &tmp);
				D.push_back(tmp);
			}
		}
		getchar();
		int forb = 1;
		int check = 0;
		for (unsigned int i = 0; i<order.size(); i++) {
			if (order[i] == 'R') {
				forb = forb * -1;
			}else{
				if (forb == 1) {
					check = D.pop_front();
				}
				else {
					check = D.pop_back();
				}
			}
		}
		if (check == -1) {
			printf("error\n"); continue;
		}
		if (D.size == 0) {
			printf("[]\n"); continue;
		}
		if (forb == 1) {
			ListNode<int>* t1 = D.head->rear;
			printf("[");
			while (t1->rear != nullptr) {
				if (t1->rear == D.tail) {
					printf("%d", t1->value); break;
				}
				printf("%d,", t1->value);
				t1 = t1->rear;
			}
			printf("]\n");
		}
		else {
			ListNode<int>* t1 = D.tail->next;
			printf("[");
			while (t1->next != nullptr) {
				if (t1->next == D.head) {
					printf("%d", t1->value); break;
				}
				printf("%d,", t1->value);
				t1 = t1->next;
			}
			printf("]\n");
		}
	}
	return 0;
}