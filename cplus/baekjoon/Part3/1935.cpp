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

template<typename T>
ostream& operator <<(ostream& out, const Stack<T>& LL) {
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


double cal(double b, double a, char c) {
	switch (c) {
	case '+':return b + a;
	case '-':return b - a;
	case '/':return b / a;
	case '*':return b * a;
	default: return 0;
	}
}

int main() {
	Stack<double> S;
	char i[103] = { 0, };
	int N;
	cin >> N;
	getchar();
	cin >> i;
	double F[26];
	for (int j = 0; j < N; j++) {
		scanf("%lf", &F[j]);
	}
	int n = 0;
	while (i[n]) {
		if (i[n] >= 'A') {
			S.push(F[i[n] - 'A']);
		}
		else {
			S.push(cal(S.pop(), S.pop(), i[n]));
		}
		n++;
	}
	printf("%.2lf", S.pop());
	return 0;
}