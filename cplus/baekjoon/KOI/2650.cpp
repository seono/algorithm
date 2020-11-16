#include<iostream>
#include<cstdlib>
#define ffor(i,x)for(int i=0;i<x;i++)
#define fffor(i,x)for(int i = 1; i<=x; i++)

int dot[50][2];
int line4[4][50];
int d_min[50];

int compare(const void* a, const void* b)
{
	int num1 = *(int*)a;
	int num2 = *(int*)b;
	if (num1 > num2)return 1;
	if (num1 < num2)return -1;
	return 0;
}
int r_compare(const void* a, const void* b)
{
	int num1 = *(int*)a;
	int num2 = *(int*)b;
	if (num1 > num2)return -1;
	if (num1 < num2)return 1;
	return 0;
}
int main() {
	int test_case;
	scanf("%d", &test_case);
	for (int i = 0; i < test_case; i++) {
		scanf("%d %d", &dot[i][0], &dot[i][1]);
		line4[dot[i][0] - 1][i] = dot[i][1];
	}
	qsort(line4[0], 50, sizeof(int), r_compare);
	qsort(line4[3], 50, sizeof(int), r_compare);
	qsort(line4[1], 50, sizeof(int), compare);
	qsort(line4[2], 50, sizeof(int), compare);
	ffor(i, test_case) {
		int cnt = 0;
		int worked = 0;
		while (1) {
			int x = 0;
			ffor(y, 50) {
				if (line4[x][y])cnt++;
				if (x + 1 == dot[i][0] && line4[x][y] == dot[i][1]) {
					worked = 1; break;
				}
			}
			if (worked)break;
			x = 2;
			ffor(y, 50) {
				if (line4[x][y])cnt++;
				if (x + 1 == dot[i][0] && line4[x][y] == dot[i][1]) {
					worked = 1; break;
				}
			}
			if (worked)break;
			x = 1;
			ffor(y, 50) {
				if (line4[x][y])cnt++;
				if (x + 1 == dot[i][0] && line4[x][y] == dot[i][1]) {
					worked = 1; break;
				}
			}
			if (worked)break;
			x = 3;
			ffor(y, 50) {
				if (line4[x][y])cnt++;
				if (x + 1 == dot[i][0] && line4[x][y] == dot[i][1]) {
					worked = 1; break;
				}
			}
			if (worked)break;
		}
		d_min[i] = cnt;
	}
	int all = 0;
	int line = 0;
	int l[50] = { 0, };
	ffor(i, test_case) {
		int l1 = d_min[i];
		int l2 = d_min[i + 1];
		int cnt = 0;
		for (int j = 0; j < test_case; j++) {
			int l3 = d_min[j];
			int l4 = d_min[j + 1];
			if (l3 < l4) {
				if (l3 < l1 && l1 < l4 && (l2<l3 || l2>l4)) {
					cnt++;
				}
				else if (l3 < l2 && l2 < l4 && (l1<l3 || l1>l4)) {
					cnt++;
				}
			}
			else {
				if (l4 < l1 && l1 < l3 && (l2<l4 || l2>l3)) {
					cnt++;
				}
				else if (l4 < l2 && l2 < l3 && (l1<l4 || l1>l3)) {
					cnt++;
				}
			}
			j++;
		}
		all += cnt;
		l[line++] = cnt;
		i++;
	}
	qsort(l, 50, sizeof(int), r_compare);
	printf("%d\n%d", all / 2, l[0]);
	return 0;
}