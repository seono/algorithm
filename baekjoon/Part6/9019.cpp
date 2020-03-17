#include<iostream>
#include<queue>
#include<vector>
using namespace std;

vector<int>visited(10000, -1);
vector<char> from(10000);

int L(int num) {
	num = num * 10;
	num = num + num / 10000;
	num %= 10000;
	return num;
}
int R(int num) {
	int temp = num % 10;
	num = num / 10 + temp * 1000;
	return num;
}
int D(int num) {
	return 2 * num % 10000;
}
int S(int num) {
	if (num == 0)return 9999;
	return num - 1;
}


int main() {
	int N;
	scanf("%d", &N);
	while (N--) {
		int A, B;
		fill(visited.begin(), visited.end(), -1);
		scanf("%d %d", &A, &B);
		queue<int> Q;
		Q.push(A);
		visited[A] = 1;
		while (!Q.empty()) {
			int temp = Q.front();
			Q.pop();
			int d, s, l, r;
			d = D(temp);
			s = S(temp);
			l = L(temp);
			r = R(temp);
			if (visited[d]==-1) {
				visited[d] = temp;
				from[d] = 'D';
				Q.push(d);
			}
			if (visited[s]==-1) {
				visited[s] = temp;
				from[s] = 'S';
				Q.push(s);
			}
			if (visited[l] == -1) {
				visited[l] = temp;
				from[l] = 'L';
				Q.push(l);
			}
			if (visited[r] == -1) {
				visited[r] = temp;
				from[r] = 'R';
				Q.push(r);
			}
			if (d == B || s == B || l == B || r == B)break;
		}
		string str = "";
		while (B != A) {
			str =from[B]+str;
			B = visited[B];
		}
		cout << str << endl;
	}
}