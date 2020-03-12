#include<iostream>
#include<vector>
using namespace std;

vector<int> hate, fav;
vector<bool>visited;

int main() {
	int N, M, P;
	scanf("%d %d %d", &N, &M, &P);
	hate.resize(M+1);
	fav.resize(N+1);
	visited.resize(M+1,false);
	for (int i = 1; i <= N; i++) {
		int h;
		scanf("%d %d", &fav[i], &h);
		if (!hate[h])hate[h] = i;
	}
	visited[P] = true;
	int cnt = 0;
	int h = P;
	while (hate[h]) {
		h = fav[hate[h]];
		cnt++;
		if (visited[h]) {
			printf("-1\n");
			return 0;
		}
		visited[h] = true;
	}
	printf("%d\n", cnt);
	return 0;
}