#include<iostream>
#include<queue>
#include<cstring>
using namespace std;
bool visited[1000002];
int main() {
	int ans = -1;
	int F, S, G, U, D;
	scanf("%d %d %d %d %d", &F, &S, &G, &U, &D);
	queue<int> Q;
	Q.push(S);
	visited[S] = true;
	while (!Q.empty()) {
		int Qsize = Q.size();
		ans++;
		for (int a = 0; a < Qsize; a++) {
			int tmp = Q.front();
			Q.pop();
			if (tmp == G) {
				printf("%d\n", ans); return 0;
			}
			if (tmp + U <= F && !visited[tmp + U]) {
				visited[tmp + U] = true;
				Q.push(tmp + U);
			}
			if (tmp - D > 0 && !visited[tmp - D]) {
				visited[tmp - D] = true;
				Q.push(tmp - D);
			}
		}
	}
	printf("use the stairs\n");
	return 0;
}