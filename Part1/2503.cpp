#include <iostream>
#pragma warning(disable:4996)
using namespace std;
#include<vector>
typedef struct stba {
	int st=0;
	int ba=0;
};

stba check(int ans, int test_num) {
	stba answer;
	int a1 = ans / 100;
	int b1 = ans / 10 % 10;
	int c1 = ans % 10;
	int a = test_num / 100;
	int b = test_num / 10 % 10;
	int c = test_num % 10;
	if (a1 == a)answer.st++;
	if (b1 == b)answer.st++;
	if (c1 == c)answer.st++;
	if (a1 == b || a1 == c)answer.ba++;
	if (b1 == a || b1 == c)answer.ba++;
	if (c1 == a || c1 == b)answer.ba++;
	return answer;
}

int main() {
	int N;
	vector<int>ans_list;
	for (int i = 1; i < 10; i++) {
		for (int j = 1; j < 10; j++) {
			for (int k = 1; k < 10; k++) {
				if (i != j && k != j && i != k) {
					ans_list.push_back(i * 100 + j * 10 + k);
				}
			}
		}
	}
	scanf("%d", &N);
	for (int a = 0; a < N; a++) {
		int ans, st, ba;
		scanf("%d %d %d", &ans, &st, &ba);
		for (int i = 0; i < ans_list.size();) {
			stba res = check(ans, ans_list[i]);
			if (!(res.st == st && res.ba == ba)) {
				ans_list.erase(ans_list.begin()+i);
			}
			else {
				i++;
			}
		}
	}
	printf("%d", ans_list.size());
	return 0;
}