#include<iostream>
#include<queue>
#include<vector>
using namespace std;

char arr[31][31][31];
int dx[6] = { 0,0,0,0,1,-1 };
int dy[6] = { 0,0,1,-1,0,0 };
int dz[6] = { 1,-1,0,0,0,0 };
struct pnt {
	int l, r, c;
};

int main() {
	int L, R, C;
	queue<pnt> Q;
	while (true) {
		scanf("%d %d %d", &L, &R, &C);
		if (L == 0 && R == 0 && C == 0)return 0;
		getchar();
		for (int k = 0; k < L; k++) {
			for (int j = 0; j < R; j++) {
				for (int i = 0; i < C; i++) {
					scanf("%c", &arr[k][j][i]);
				}
				getchar();
			}
			getchar();
		}
		int worked = 0;
		for (int k = 0; k < L; k++) {
			for (int j = 0; j < R; j++) {
				for (int i = 0; i < C; i++) {
					if (arr[k][j][i] == 'S') {
						int ans = 0;
						pnt tmp;
						tmp.l = k;
						tmp.r = j;
						tmp.c = i;
						Q.push(tmp);
						arr[k][j][i] = '#';
						while (!Q.empty()) {
							ans++;
							int Qsize = Q.size();
							for (int t = 0; t < Qsize; t++) {
								pnt temp = Q.front();
								Q.pop();
								for (int a = 0; a < 6; a++) {
									int x = temp.c + dx[a];
									int y = temp.r + dy[a];
									int z = temp.l + dz[a];
									if (x < 0 || x >= C || y < 0 || y >= R || z < 0 || z >= L)continue;
									if (arr[z][y][x] == 'E') {
										printf("Escaped in %d minute(s).\n", ans);
										worked = 1;
										while (!Q.empty())Q.pop();
										break;
									}
									if (arr[z][y][x] == '.') {
										arr[z][y][x] = '#';
										pnt temp2;
										temp2.c = x;
										temp2.r = y;
										temp2.l = z;
										Q.push(temp2);
									}
								}
								if (worked)break;
							}
							if (worked)break;
						}
						if (worked)break;
					}
					if (worked)break;
				}
				if (worked)break;
			}
			if (worked)break;
		}
		if (worked)continue;
		else printf("Trapped!\n");
	}
	return 0;
}