#include<iostream>
#include<cstdlib>
#include<stack>
using namespace std;


int main() {
	stack<int> S;
	stack<int> sort_S;
	for (int i = 0; i < 20; i++) {
		int a = rand() % 50 + 1;
		S.push(a);
		sort_S.push(a);
	}
	for (int i = 0; i < 20; i++) {
		cout << S.top()<<" "; S.pop();
	}
	return 0;
}