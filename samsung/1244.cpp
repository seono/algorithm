/////////////////////////////////////////////////////////////////////////////////////////////
// �⺻ �����ڵ�� ���� �����ص� ���� �����ϴ�. ��, ����� ���� ����
// �Ʒ� ǥ�� ����� ���� �ʿ�� �����ϼ���.
// ǥ�� �Է� ����
// int a;
// float b, c;
// double d, e, f;
// char g;
// char var[256];
// long long AB;
// cin >> a;                            // int ���� 1�� �Է¹޴� ����
// cin >> b >> c;                       // float ���� 2�� �Է¹޴� ���� 
// cin >> d >> e >> f;                  // double ���� 3�� �Է¹޴� ����
// cin >> g;                            // char ���� 1�� �Է¹޴� ����
// cin >> var;                          // ���ڿ� 1�� �Է¹޴� ����
// cin >> AB;                           // long long ���� 1�� �Է¹޴� ����
/////////////////////////////////////////////////////////////////////////////////////////////
// ǥ�� ��� ����
// int a = 0;                            
// float b = 1.0, c = 2.0;               
// double d = 3.0, e = 0.0; f = 1.0;
// char g = 'b';
// char var[256] = "ABCDEFG";
// long long AB = 12345678901234567L;
// cout << a;                           // int ���� 1�� ����ϴ� ����
// cout << b << " " << c;               // float ���� 2�� ����ϴ� ����
// cout << d << " " << e << " " << f;   // double ���� 3�� ����ϴ� ����
// cout << g;                           // char ���� 1�� ����ϴ� ����
// cout << var;                         // ���ڿ� 1�� ����ϴ� ����
// cout << AB;                          // long long ���� 1�� ����ϴ� ����
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
	//0ȸ�� input
	if (stoi(input) == v[0]) {
		for (int a = 0; a < input.size(); a++) {
			if (input[a] == input[a + 1]) {
				v.clear();
				v.push_back(stoi(input));
				v.push_back(stoi(input));
				//�ִ��� input���� ���� ���ڰ� ������ ���� Ƚ�� ������� input�� �ִ�
				return;
			}
		}
		//�ٲٱ� ���Ҵµ� input�� �ִ��϶�
		v.clear();
		int temp = input[input.size() - 1];
		//temp�� input ��������
		input[input.size() - 1] = input[input.size() - 2];
		input[input.size() - 2] = temp;
		//���������� ���������� �ι�°�� swap
		v.push_back(stoi(input));
		v.push_back(stoi(input));
		return;
	}
	//input�� �ִ밡 �ƴҶ�
	//�ռ������� max�� change�Ǿ��ִ°͵� ����
	for (a=a+1; a < input.size(); a++) {
		if (input[max] < input[a])max = a;
	}
	//max�� �̹� ��ġ�Ǿ�������� �������� �Ѿ��
	if (max == first) {
		change_str(v, c_num, input, first + 1);
		return;
	}
	//�ƴ� first�������� max�� idx��� first�� �ٲٰ� bfs
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
		//�ִ뱸�ؼ� v���־����
		change_str(v, c_num, input, 0);
		int max = 1;
		for (int a = 2; a < v.size(); a++) {
			if (v[a] > v[max])max = a;
		}
		//v���� 0�������ϰ� 1���� �˻��ؼ� �ִ�ã��
		cout <<"#"<<test_case<<" " <<v[max] << endl;
		v.clear();
	}
	return 0;//��������� �ݵ�� 0�� �����ؾ��մϴ�.
}