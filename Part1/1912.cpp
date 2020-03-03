#include<iostream>
#pragma warning(disable:4996)
#include<algorithm>
#include<vector>
using namespace std;

int main() {
    int N;
    scanf("%d", &N);
    vector<int>arr(N);
    vector<int>dp(N);
    for (int i = 0; i < N; i++) {
        scanf("%d", &arr[i]);
    }
    dp[0] = arr[0];
    int maxi = arr[0];
    for (int i = 1; i < N; i++) {
        dp[i] = max(arr[i], arr[i] + dp[i - 1]);
        maxi = max(dp[i], maxi);
    }
    printf("%d", maxi);
    return 0;
}