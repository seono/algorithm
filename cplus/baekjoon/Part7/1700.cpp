#include<iostream>
#include<vector>
#include<set>
using namespace std;

int main() {
	int N, K;
	int C_size = 0;
	scanf("%d %d", &N, &K);
	vector<int> arr(K);
	//-1이 없는상태
	vector<int> C(K + 1, -1);
	//앞으로 남은 횟수
	int cnt[101] = { 0, };
	for (int i = 0; i < K; i++) {
		scanf("%d", &arr[i]);
		cnt[arr[i]]++;
	}
	int i;
	for (i = 0; C_size < N; i++) {
		cnt[arr[i]]--;
		//자리가 남아있는경우
		if (C[arr[i]] == -1) {
			C[arr[i]] = cnt[arr[i]];
			C_size++;
		}
		//원래 있는경우
		else {
			C[arr[i]]--;
		}
	}
	int ans = 0;
	for (; i < K; i++) {
		//원래 있는경우
		cnt[arr[i]]--;
		if (C[arr[i]] > -1) {
			C[arr[i]]--;//남은 횟수 줄임
		}
		//빼야하는 경우
		else {
			bool er = true;
			ans++;
			//남은 횟수가 0이면 바로 제거
			for (int a = 0; a < K; a++) {
				if (C[arr[a]] == 0) {
					er = false;
					C[arr[a]]--;//0에서 -1되니까 제거
					break;
				}
			}
			//아니면 가장 나중에 나타나는 가전기기 제거
			if (er) {
				set<int> plug;
				int j;
				for (j = i + 1; plug.size() < N; j++) {
					if (C[arr[j]]>-1 && !plug.count(arr[j])) {
						plug.insert(arr[j]);
					}
				}
				j--;
				C[arr[j]] = -1;//-1로바로 수정해서 제거
			}
			C[arr[i]] = cnt[arr[i]];
		}
	}
	printf("%d", ans);
	return 0;
}