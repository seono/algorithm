#include<iostream>
#include<cstdlib>
using namespace std;

template<typename T>
class ListNode {
public:
	T value;
	ListNode<T>* next;
	ListNode<T>() : next(nullptr){}
	ListNode<T>(T value1, ListNode<T>*next1):value(value1), next(next1){}
};

template<typename T>
class Queue {
public:
	int size;
	ListNode<T>* head;
	ListNode<T>* tail;
	Queue<T>():size(0), head(nullptr), tail(nullptr){}

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
	Queue<int> Q;
	while (N--) {
		char key[8];
		//getchar();
		scanf("%s", &key);
		switch (key[0])
		{
		case 'p':
			if (key[1] == 'u') {
				int d;
				scanf("%d\n", &d);
				Q.push(d);
			}
			else {
				printf("%d\n", Q.pop());
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