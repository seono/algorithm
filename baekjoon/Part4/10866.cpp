#include<iostream>
#include<cstdlib>
using namespace std;

template <typename T>
class ListNode {
public:
	T value;
	ListNode<T>* next, * rear;
	ListNode<T>() : next(nullptr), rear(nullptr) {}
	ListNode<T>(T value1,ListNode<T>* next1,ListNode<T>* rear1):value(value1),next(next1),rear(rear1){}
};

template<typename T>
class Deque {
public:
	int size;
	ListNode<T>* head, *tail;
	Deque<T>() : size(0), head(nullptr), tail(nullptr) {}

	~Deque<T>() {
		ListNode<T>* t1=tail,* t2;
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
			ListNode<T>* t1 = new ListNode<T>(value, head,nullptr);
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
			head->rear  = t1->rear;
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
		if (size == 0)return 1;
		else return 0;
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

template<typename T>
ostream& operator <<(ostream& out, const Deque<T>& LL) {
	ListNode<T>* temp = LL.head;
	out << "front [";
	for (int i = 0; i < LL.size; i++) {
		temp = temp->rear;
		out << temp->value;
		if (i < LL.size - 1)out << ", ";
	}
	out << "] rear";
	return out;
}

int main() {
	int N;
	scanf("%d", &N);
	Deque<int> Q;
	while (N--) {
		char key[12];
		//getchar();
		scanf("%s", &key);
		switch (key[0])
		{
		case 'p':
			if (key[1] == 'u') {
				int d;
				scanf("%d", &d);
				if (key[5] == 'f') Q.push_front(d);
				else Q.push_back(d);
			}
			else {
				if (key[4] == 'f')printf("%d\n",Q.pop_front());
				else printf("%d\n", Q.pop_back());
			}break;
		case 's':printf("%d\n", Q.size);
			break;
		case 'e':if (Q.empty())printf("1\n");
				else printf("0\n");
			break;
		case 'f': printf("%d\n", Q.front());
			break;
		case 'b': printf("%d\n", Q.back());
			break;
		default:
			break;
		}
	}
	return 0;
}