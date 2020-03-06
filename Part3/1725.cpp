#include<iostream>
#include<cstdlib>
using namespace std;
typedef long long ll;

template<typename T>
class ListNode {
public:
	T value;
	int pos;
	ListNode<T>* next;
	ListNode<T>() : next(nullptr) {}
	ListNode<T>(T value1, ListNode<T>* next1) : value(value1), next(next1) {}
	ListNode<T>(T value1, int p, ListNode<T>* next1) : value(value1), pos(p), next(next1) {}
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
	void push(T value, int pos) {
		if (size == 0)head = new ListNode<T>(value, pos, nullptr);
		else {
			ListNode<T>* t1 = new ListNode<T>(value, pos, nullptr);
			t1->next = head;
			head = t1;
		}
		size++;
	}
	T top() {
		if (size == 0)return -1;
		return head->value;
	}
	int pos() {
		return head->pos;
	}
	T pop() {
		ListNode<T>* temp = head;
		T t = head->value;
		head = head->next;
		delete temp;
		size--;
		return t;
	}
};

int main() {
	Stack<ll> t;
	int N;
	scanf("%d", &N);
	t.push(0, 0);
	ll r = 0;
	int pos = 0;
	for (int i = 1; i <= N; i++) {
		ll tmp;
		scanf("%lld", &tmp);
		if (tmp > t.top()) {
			t.push(tmp, i);
			pos++;
		}
		else {
			int t_tmp = i;
			while (t.top() >= tmp) {
				int p = t.pos();
				ll tmp1 = t.pop();
				if (tmp1 == tmp) {
					t_tmp = p;
				}
				if (tmp1 * (i - p) > r)r = tmp1 * (i - p);
			}
			t.push(tmp, t_tmp);
		}
	}
	if (t.top()) {
		while (t.top() >= 0) {
			int p = t.pos();
			ll tmp1 = t.pop();
			if (tmp1 * (N + 1 - p) > r)r = tmp1 * (N + 1 - p);
		}
	}
	cout << r;
	return 0;
}