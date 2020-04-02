#include<cstdio>
int dp[11][221] = { 1 }, n, m, k;
int main() {
    scanf("%d %d %d", &n, &m, &k);
    for (int i = 1; i <= n; i++)
        for (int j = i; j <= m; j++)
            dp[i][j] = dp[i][j - i] + dp[i - 1][j - 1];
    for (int i = 1; n--, m--;) {
        for (; k > dp[n][m]; i++) k -= dp[n][m], m -= n + 1;
        printf("%d ", i);
    }
    return 0;
}