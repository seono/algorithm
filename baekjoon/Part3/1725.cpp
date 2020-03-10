#include<iostream>
#include<cstdlib>
using namespace std;
typedef long long ll;

template<typename T>
class ListNode {
public:
	T value;
	ListNode<T>* next;
	ListNode<T>() : next(nullptr) {}
	ListNode<T>(T value1, ListNode<T>* next1) : value(value1), next(next1) {}
	ListNode<T>(T value1, int p, ListNode<T>* next1) : value(value1), next(next1) {}
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
	T top() {
		if (size == 0)return -1;
		return head->value;
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
	ll* arr = new ll[N + 2];
	arr[0] = 0;
	arr[N + 1] = 0;
	for (int i = 1; i <= N; i++) {
		scanf("%lld", &arr[i]);
	}
	t.push(0);
	ll r = 0;
	//������������ ����
	//stack top�� ���鼭 height�� ����
	//�������� �����̾�����
	//���δ� stack���� ��� �� index���� index����(t.top())���� index����(i-1) 
	//���δ� ����� height�� ���簢���� ���������.
	for (int i = 1; i <= N+1; i++) {
		while (t.head&&arr[t.top()] > arr[i]) {
			ll height = arr[t.top()];
			t.pop();
			ll width = i - t.top()-1;
			ll ans = height * width;
			r = r > ans ? r : ans;
		}
		t.push(i);
	}
	cout << r << endl;
	return 0;
}