#include<iostream>
#include<cstdlib>
using namespace std;

template<typename T>
class ListNode {
public:
	T value;
	ListNode<T>* next;
	ListNode<T>():next(nullptr){}
	ListNode<T>(T value1, ListNode<T>* next1):value(value1), next(next1){}
};

template<typename T>
class Stack {
public:
	int size;
	ListNode<T>* head;
	Stack<T>():size(0), head(nullptr){}

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

int check(char s) {
	switch (s)
	{
	case '(': case')':
		return 0;
	case '+':case'-':
		return 1;
	case '*':case'/':
		return 2;
	default:
		return -1;
	}
}

int main() {
	Stack<char> S;
	char i[103] = { 0, };
	cin >> i;
	int num = 0;
	while (i[num])num++;
	int temp = -1;
	while (temp++ != num) {
		char t;
		if (i[temp]) {
			t = i[temp];
			switch (check(t))
			{
			case 0:if (t == '(')S.push(t);
				  else {
				while (S.top() != '(')cout << S.pop();
				S.pop();
			}break;
			case 1:case 2:
				while (S.top() != -1 && check(S.top()) >= check(t))cout << S.pop();
				S.push(t); break;
			case -1:
				cout << i[temp];
				break;
			default:
				break;
			}
		}
	}
	while (S.top() != -1)cout << S.pop();
	cout << endl;
	return 0;
}