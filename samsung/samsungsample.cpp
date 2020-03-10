#include<iostream>
#include<vector>
#include<cstring>
#include<utility>
#pragma warning(disable:4996)
using namespace std;
vector <pair<int, int> >cores;
int line_max, core_max, s;
bool visited[12][12];
int arr[12][12];
int dx[] = { -1,1,0,0 };
int dy[] = { 0,0,-1,1 };

void check(int startidx, int line_cnt, int core_cnt) {
	if (startidx == (int)cores.size()) {
		if (core_cnt > core_max) {
			line_max = line_cnt;
			core_max = core_cnt;
		}
		else if (core_cnt == core_max && line_cnt<line_max) {
			line_max = line_cnt;
		}
		return;
	}

	bool temp[12][12];
	for (int i = 0; i < s; i++) {
		for (int j = 0; j < s; j++) {
			temp[i][j] = visited[i][j];
		}
	}

	int x = cores[startidx].first;
	int y = cores[startidx].second;
	for (int i = 0; i < 4; i++) {
		int nx = x + dx[i];
		int ny = y + dy[i];
		int temp_len=0;
		bool linechk = true;
		while (true) {
			if (0 > nx || nx >= s || ny < 0 || ny >= s)break;
			if (arr[nx][ny] == 1 || visited[nx][ny] == true) {
				linechk = false; break;
			}
			visited[nx][ny] = true;
			nx += dx[i];
			ny += dy[i];
			temp_len++;
		}
		//연결된경우
		if (linechk) {
			check(startidx + 1, line_cnt + temp_len, core_cnt + 1);
		}
		//연결시도하다 막힌경우
		if (temp_len > 0) {
			for (int a = 0; a < s; a++) {
				for (int b = 0; b < s; b++) {
					visited[a][b] = temp[a][b];
				}
			}
		}
	}
	//연결안하고 그냥 패스
	check(startidx + 1, line_cnt, core_cnt);
}
int main(int argc, char** argv)
{
	int test_case;
	int T;
	freopen("input.txt", "r", stdin);
	scanf("%d", &T);
	for (test_case = 1; test_case <= T; ++test_case)
	{
		scanf("%d", &s);
		for (int i = 0; i < s; i++) {
			for (int j = 0; j < s; j++) {
				scanf("%d", &arr[i][j]);
				if (arr[i][j] == 1 &&
					(i > 0 && i < s - 1 && j>0 && j < s - 1)) {
					cores.emplace_back(make_pair(i, j));
				}
			}
		}
		check(0, 0, 0);
		printf("#%d %d\n", test_case, line_max);
		core_max = 0;
		line_max = 0;
		memset(arr, 0, sizeof(arr));
		memset(visited, 0, sizeof(visited));
		cores.clear();
	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}