#include<iostream>
#include<queue>
#include<vector>
#include<string>
using namespace std;

//�־��� ���� �̹� max�ε� chance�� �������
//���� ������ 2���� �ִ� ���϶�
//�ƴҋ�
//max�� �ƴҶ�
//���� first(���� ū �ڸ����� ���� ū ���� �ְ� ������ �ѱ�ٸ� first �� ���� �ڸ���)
//first�� ���� ū ���ڰ� ���µ� ��� �ڸ��� �ִ� ���ڵ� �� ����ְ�

void check(vector<int>& v, int chance, int first, string num) {
	if (chance == 0) {
		v.push_back(stoi(num));
		return;
	}
	if (stoi(num) == v[0]) {
		for (unsigned int i = 0; i < num.size()-1; i++) {
			if (num[i] == num[i + 1]) {
				v.clear();
				v.push_back(stoi(num));
				v.push_back(stoi(num));
				return;
			}
		}
		if (chance % 2 == 0)return;
		v.clear();
		int temp = num[num.size() - 1];
		num[num.size() - 1] = num[num.size() - 2];
		num[num.size() - 2] = temp;
		v.push_back(stoi(num));
		v.push_back(stoi(num));
		return;
	}
	int max = first;
	for (unsigned int a = first + 1; a < num.size(); a++) {
		if (num[a] > num[max])max = a;
	}
	if (first == max) {
		check(v, chance, first + 1, num);
		return;
	}
	for (unsigned int x = first; x < num.size(); x++) {
		if (num[x] == num[max]) {
			string t_str = num;
			int temp = t_str[x];
			t_str[x] = t_str[first];
			t_str[first] = temp;
			check(v, chance - 1, first + 1, t_str);
		}
	}
	return;
}

int main() {
	string M;
	cin >> M;
	string temp = M;
	int K;
	cin >> K;
	if (stoi(M)<=10||(stoi(M)<100&&M[1]=='0')) {
		cout << "-1" << endl; return 0;
	}
	for (unsigned int i = 0; i < temp.length(); i++) {
		int m = i;
		for (unsigned int j = i + 1; j < temp.length(); j++) {
			if (temp[m] < temp[j])m = j;
		}
		int t = temp[m];
		temp[m] = temp[i];
		temp[i] = t;
	}
	vector<int> v;
	v.push_back(stoi(temp));
	check(v, K, 0, M);
	int m = 1;
	if (v.size() == 1)cout << v[0] << endl;
	else {
		for (unsigned int i = 1; i < v.size(); i++) {
			if (v[i] > v[m])m = i;
		}
		cout << v[m] << endl;
	}
	return 0;
}