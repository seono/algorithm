#include<iostream>
#include<cstdlib>
#include <cstring>

using namespace std;

template<typename T>
class ListNode {
public:
	T value;
	ListNode<T>* next;
	ListNode<T>() : next(nullptr){}
	ListNode<T>(T value1, ListNode<T>* next1) : value(value1), next(next1){}
};

template<typename T>
class Stack {
public:
	int size;
	ListNode<T>* head;
	Stack<T>() : size(0), head(nullptr){}
	
	~Stack<T>() {
		ListNode<T>* t1 = head,* t2;
		while (t1 != nullptr) {
			t2 = t1->next;
			delete t1;
			t1 = t2;
		}
	}
	void push(T value) {
		if (size == 0) head = new ListNode<T>(value, nullptr);
		else {
			ListNode<T>* t1 = new ListNode<T>(value, nullptr);
			t1->next = head;
			head = t1;
		}
		size++;
	}
	T top() {
		return head->value;
	}
	T pop(){
		ListNode<T>* t1 = head;
		T tmp = t1->value;
		head = head->next;
		delete t1;
		return tmp;
	}
};

int check(char* word1, char* word2) {
	int pos = 0;
	while (word1[pos+1] && word1[pos+1]!='>' && word2[pos] != '>') {
		if (word1[pos+1] != word2[pos])return 0;
		pos++;
	}
	return 1;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	while (true) {
		char str[300];
		Stack<char*> S;
		cin.getline(str,300);
		if (str[0] == '#')return 0;
		char* word = strchr(str, '<');
		if (word != nullptr)word = word + 1;
		while (word != nullptr) {
			if (word[0] == '/') {
				if (S.head == nullptr) {
					S.push(word); break;
				}
				if (check(word, S.top()))S.pop();
				else {
					S.push(word); break;
				}
			}
			else if (word[0] == 'b' && word[1] == 'r') {
				word = strchr(word + 1, '<');
				if (word != nullptr)word = word + 1;
				continue;
			}
			else S.push(word);
			if(word[1])word = strchr(word + 1, '<');
			if (word != nullptr)word = word + 1;
		}
		if (S.head==nullptr)cout << "legal" << endl;
		else cout << "illegal" << endl;
	}
	return 0;
}