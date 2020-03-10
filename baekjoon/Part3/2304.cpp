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

/*
왼쪽에서도 오름차순 오른쪽에서 오름차순
*/


int main() {
	int N;
	Stack<int> S;
	int ans = 0;
	int arr[1002]={ 0, };
	scanf("%d", &N);
	if (N == 0) {
		puts("0"); return 0;
	}
	for (int i = 0; i < N; i++) {
		int pos;
		scanf("%d", &pos);
		scanf("%d", &arr[pos]);
	}
	int longest=0, end=1000;
	int start = 0;
	while (arr[start]==0)start++;
	while (arr[end]==0)end--;
	int tmp = 0;
	while (tmp < 1001) {
		if (arr[longest] < arr[tmp])longest = tmp;
		tmp++;
	}
	S.push(arr[start]);
	for (int i = start; i <= longest; i++) {
		if (arr[i] > S.top())S.push(arr[i]);
		ans += S.top();
	}
	S.push(arr[end]);
	for (int i = end; i > longest; i--) {
		if (arr[i] > S.top())S.push(arr[i]);
		ans += S.top();
	}
	printf("%d", ans);
	return 0;
}