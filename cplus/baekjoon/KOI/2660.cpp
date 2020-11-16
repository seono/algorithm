#include<iostream>
#define ffor(i,x)for(int (i)=0;(i)<(x);(i)++)
#define fffor(i,x)for(int (i)=1;i<=x;i++)

using namespace std;

#pragma warning(disable:4996)
int arr[51][51];
int cnt[51];
int main() {
	int p;
	scanf("%d", &p);
	int a, b;
	scanf("%d %d", &a, &b);
	while (a != -1) {
		arr[a][b] = 1;
		arr[b][a] = 1;
		scanf("%d %d", &a, &b);
	}
	fffor(k, p) {
		int people = p;
		int que[100] = { 0, };
		int is[51] = { 0, };
		int num = 0;
		int first = 0;
		int size = 0;
		que[first] = k;
		is[k] = 1;
		size++; people--;
		if (people == 0) {
			printf("0\n");
		}
		while (people > 0) {
			int s = size;
			for (int a = 0; a < s; a++) {
				for (int j = 1; j <= p; j++) {
					if (arr[j][que[first % 100]] == 1 && is[j] == 0) {
						is[j] = 1;
						people--;
						que[(first + size++) % 100] = j;
					}
				}
				size--;
				first++;
			} num++;
		}
		cnt[k] = num;
	}
	int min=1;
	int min_p=0;
	fffor(i, p) {
		if (cnt[i] < cnt[min])min = i;
	}
	fffor(i, p) {
		if (cnt[i] == cnt[min])min_p++;
	}
	printf("%d %d\n", cnt[min], min_p);
	fffor(i, p) {
		if (cnt[i] == cnt[min])printf("%d ", i);
	}
	return 0;
}