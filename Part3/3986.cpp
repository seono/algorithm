#include<iostream>
#include<vector>

char st[100002];
int n = 0;
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    int N;
    cin >> N;
    st[0] = 0;
    int ans = 0;
    for (int i = 0; i < N; i++) {
        string str;
        cin >> str;
        n = 1;
        for (int si = 0; si < str.size(); si++) {
            if (st[n - 1] == str[si]) {
                n--;
            }
            else {
                st[n] = str[si];
                n++;
            }
        }
        if (n == 1)ans++;
    }
    printf("%d", ans);
    return 0;
}