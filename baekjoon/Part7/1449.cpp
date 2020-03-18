#include<iostream>
#include<algorithm>
using namespace std;

int main() {
	int N, L;
	scanf("%d %d", &N, &L);
	int* arr = new int[N];
	for (int i = 0; i < N; i++) {
		scanf("%d", &arr[i]);
	}
	sort(arr, arr + N);
	int ans = 0;
	for (int i = 0; i < N - 1;) {
		int first = arr[i];
		int next = arr[i + 1];
		//next에 i=N-1까지 검사
		while (i<N-1&&next - first <= L - 1) {
			i++;
			next = arr[i+1];
		}
		ans++;
		//next에 N-1까지 한번에 붙는 경우
		if (i == N-1)break;
		i++;
		//next에 N-2까지 한번에 붙었을 때
		if (i == N-1) {
			ans++;
		}
	}
	if (N == 1)printf("1");
	else printf("%d", ans);
	return 0;
}