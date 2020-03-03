#include <iostream>
#pragma warning(disable:4996)
#include<vector>
#include<algorithm>
using namespace std;
int N;
vector<vector<int>>arr(50, vector<int>(50, 0));
vector<vector<int>>temp_arr(50, vector<int>(50, 0));
int num = 0;
int m_line = 1;
int dx[] = { 0,0,1,-1 };
int dy[] = { 1,-1,0,0 };
void finding(int temp) {
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			int t = 0;
			if ((int)temp_arr[i][j] == temp) {
				while (j + t < N && temp_arr[i][j]==temp_arr[i][j + t])t++;
				if (t > m_line)m_line = t;
				t = 0;
				while (i + t < N && temp_arr[i][j] == temp_arr[i+t][j])t++;
				if (t > m_line)m_line = t;
			}
		}
	}
	return;
}
void check(int a, int b) {
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			temp_arr[i][j] = arr[i][j];
		}
	}
	for (int i = 0; i < 4; i++) {
		int temp = temp_arr[a][b];
		if (a + dx[i] >= 0 && a + dx[i] < N && b + dy[i] >= 0 && b + dy[i] < N) {
			temp_arr[a][b] = temp_arr[a + dx[i]][b + dy[i]];
			temp_arr[a + dx[i]][b + dy[i]] = temp;
			finding(temp);
			temp = temp_arr[a][b];
			temp_arr[a][b] = temp_arr[a + dx[i]][b + dy[i]];
			temp_arr[a + dx[i]][b + dy[i]] = temp;
		}
	}
	return;
}
int main() {
	scanf("%d", &N);
	getchar();
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			char a;
			scanf("%c", &a);
			arr[i][j] = a;
		}
		getchar();
	}
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			check(i, j);
		}
	}
	printf("%d", m_line);
	return 0;
}