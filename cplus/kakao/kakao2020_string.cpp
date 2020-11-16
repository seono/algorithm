#include <string>
#include <vector>

using namespace std;

int solution(string s) {
    int s_len = s.length();
    int min_len = s_len;
    for (int i = 1; i <= s_len / 2; i++) {
        int tmp_len = 0;
        for (int j = 0; j < s_len - 1;) {
            int d = 0;
            while (j < s_len) {
                d++;
                int a = 1;
                for (int t = 0; t < i; t++) {
                    if (s[j + t] != s[j + i + t]) {
                        a = 0;
                        break;
                    }
                }
                j += i;
                if (a == 0)break;
            }
            tmp_len += i;
            if (d != 1) {
                if (d < 10) tmp_len++;
                else if (d < 100)tmp_len += 2;
                else tmp_len += 3;
            }
            if (j<s_len && j + 2 * i>s_len) {
                tmp_len += (s_len - j);
                break;
            }
        }
        if (tmp_len < min_len)min_len = tmp_len;
    }
    int answer = min_len;
    return answer;
}