#include <string>
#include <vector>
#include <stack>
#include<iostream>
using namespace std;

typedef struct str {
    string u;
    string v;
}p_str;

p_str parser(string p) {
    p_str r_str;
    int l = 0, r = 0;
    for (int i = 0; i < p.length(); i++) {
        r_str.u.push_back(p[i]);
        if (p[i] == '(')l++;
        else r++;
        if (l == r) {
            i++;
            while (i < p.length()) {
                r_str.v.push_back(p[i]);
                i++;
            }
            break;
        }
    }
    return r_str;
}

int clear_str(string u) {
    stack<char> S;
    for (int i = 0; i < u.length(); i++) {
        if (u[i] == '(') {
            S.push(u[i]);
        }
        else {
            if (S.size() == 0)return -1;
            if (S.top() == '(')S.pop();
            else return -1;
        }
    }
    return 1;
}

string solution(string p) {
    string answer = "";
    if (p.length() == 0) return answer;
    p_str r_str = parser(p);
    if (clear_str(p) == 1)return p;
    if (clear_str(r_str.u) == 1) {
        r_str.u.append(solution(r_str.v));
        return r_str.u;
    }
    else {
        answer.push_back('(');
        answer.append(solution(r_str.v));
        answer.push_back(')');
        for (int i = 1; i < r_str.u.length() - 1; i++) {
            if (r_str.u[i] == '(')answer.push_back(')');
            else answer.push_back('(');
        }
    }
    return answer;
}

int main() {
    cout<<solution(")(");
    return 0;
}