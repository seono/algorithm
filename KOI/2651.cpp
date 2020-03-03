#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <malloc.h>
#include <string.h>

#define INF 987654321

int n, m;
int p[105];
int djk[105];
int idx;
int ans[105];

int dismax;
int cntdis;
int map[2][105];

int anscnt;

void dfs()
{
	int x;
	int i, j;

	for (i = 0; i < n + 1; ++i) {
		cntdis = 0;
		for(int a=0;a<=n+1;a++)printf("%d ", djk[a]);
		printf("\n");
		for (j = i + 1; j <= n + 1; ++j) {
			cntdis += map[0][j - 1];
			if (cntdis <= dismax) {
				if (djk[j] > djk[i] + map[1][j]) {
					djk[j] = djk[i] + map[1][j];
					p[j] = i;
				}
			}
			else {
				break;
			}
		}
	}

}

int main(void)
{
	int i, j, k;
	int u, v, w;

	scanf("%d", &dismax);
	scanf("%d", &n);
	for (i = 0; i <= n; ++i) {
		scanf("%d", &map[0][i]);
		djk[i] = INF;
	}
	djk[n + 1] = INF;
	for (i = 1; i <= n; ++i) {
		scanf("%d", &map[1][i]);
	}
	djk[0] = 0;
	dfs();

	idx = 0;
	printf("%d\n", djk[n + 1]);
	if (djk[n + 1] == 0) {
		printf("0");
	}
	else {
		int start = n + 1;
		while (p[start] != 0) {
			ans[++idx] = p[start];
			start = p[start];
		}


		printf("%d\n", idx);
		for (i = idx; i >= 1; --i) {
			printf("%d ", ans[i]);
		}
	}

	return 0;

}