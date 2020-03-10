/////////////////////////////////////////////////////////////////////////////////////////////
// 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
// 아래 표준 입출력 예제 필요시 참고하세요.
// 표준 입력 예제
// int a;
// float b, c;
// double d, e, f;
// char g;
// char var[256];
// long long AB;
// cin >> a;                            // int 변수 1개 입력받는 예제
// cin >> b >> c;                       // float 변수 2개 입력받는 예제 
// cin >> d >> e >> f;                  // double 변수 3개 입력받는 예제
// cin >> g;                            // char 변수 1개 입력받는 예제
// cin >> var;                          // 문자열 1개 입력받는 예제
// cin >> AB;                           // long long 변수 1개 입력받는 예제
/////////////////////////////////////////////////////////////////////////////////////////////
// 표준 출력 예제
// int a = 0;                            
// float b = 1.0, c = 2.0;               
// double d = 3.0, e = 0.0; f = 1.0;
// char g = 'b';
// char var[256] = "ABCDEFG";
// long long AB = 12345678901234567L;
// cout << a;                           // int 변수 1개 출력하는 예제
// cout << b << " " << c;               // float 변수 2개 출력하는 예제
// cout << d << " " << e << " " << f;   // double 변수 3개 출력하는 예제
// cout << g;                           // char 변수 1개 출력하는 예제
// cout << var;                         // 문자열 1개 출력하는 예제
// cout << AB;                          // long long 변수 1개 출력하는 예제
/////////////////////////////////////////////////////////////////////////////////////////////
#pragma warning(disable:4996)
#include <vector>
#include <iostream>
#include<string>
using namespace std;
vector<int> v;

void change_str(vector<int> &v, int c_num, string& input, int first) {
	int max = first;
	int a = first;
	if (c_num == 0) {
		v.push_back(stoi(input));
		return;
	}
	if (stoi(input) == v[0]) {
		for (int a = 0; a < input.size(); a++) {
			if (input[a] == input[a + 1]) {
				v.clear();
				v.push_back(stoi(input));
				v.push_back(stoi(input));
				return;
			}
		}
		v.clear();
		int temp = input[input.size() - 1];
		input[input.size() - 1] = input[input.size() - 2];
		input[input.size() - 2] = temp;
		v.push_back(stoi(input));
		v.push_back(stoi(input));
		return;
	}
	for (a=a+1; a < input.size(); a++) {
		if (input[max] < input[a])max = a;
	}
	if (max == first) {
		change_str(v, c_num, input, first + 1);
		return;
	}
	for (int x = first; x < input.size(); x++) {
		if (input[x] == input[max]) {
			string t_input = input;
			int temp = t_input[first];
			t_input[first] = input[x];
			t_input[x] = temp;
			change_str(v, c_num - 1, t_input, first + 1);
		}
	}
}

int main(int argc, char** argv)
{
	int test_case;
	int T;
	freopen("input.txt", "r", stdin);
	cin >> T;
	for (test_case = 1; test_case <= T; ++test_case)
	{
		string input, t;
		cin >> input;
		t = input;
		int c_num;
		cin >> c_num;
		for (int a = 0; a < input.size(); a++) {
			int max = a;
			for (int i = a + 1; i < input.size(); i++) {
				if (t[max] < t[i])max = i;
			}
			int temp = t[max];
			t[max] = t[a];
			t[a] = temp;
		}
		v.push_back(stoi(t));
		change_str(v, c_num, input, 0);
		int max = 1;
		for (int a = 2; a < v.size(); a++) {
			if (v[a] > v[max])max = a;
		}
		cout <<"#"<<test_case<<" " <<v[max] << endl;
		v.clear();
	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}