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
#include<iostream>
#include<string>
#include<vector>
using namespace std;

int pow(int i) {
	int a = 1;
	for (int x = 0; x < i; x++) {
		a = a * 2;
	}
	return a;
}

int main(int argc, char** argv)
{
	int test_case;
	int T;
	/*
	   �Ʒ��� freopen �Լ��� input.txt �� read only �������� �� ��,
	   ������ ǥ�� �Է�(Ű����) ��� input.txt ���Ϸκ��� �о���ڴٴ� �ǹ��� �ڵ��Դϴ�.
	   //�������� �ۼ��� �ڵ带 �׽�Ʈ �� ��, ���Ǹ� ���ؼ� input.txt�� �Է��� ������ ��,
	   freopen �Լ��� �̿��ϸ� ���� cin �� ������ �� ǥ�� �Է� ��� ���Ϸκ��� �Է��� �޾ƿ� �� �ֽ��ϴ�.
	   ���� �׽�Ʈ�� ������ ������ �Ʒ� �ּ��� ����� �� �Լ��� ����ϼŵ� �����ϴ�.
	   freopen �Լ��� ����ϱ� ���ؼ��� #include <cstdio>, Ȥ�� #include <stdio.h> �� �ʿ��մϴ�.
	   ��, ä���� ���� �ڵ带 �����Ͻ� ������ �ݵ�� freopen �Լ��� ����ų� �ּ� ó�� �ϼž� �մϴ�.
	*/
	freopen("input.txt", "r", stdin);
	cin >> T;
	/*
	   ���� ���� �׽�Ʈ ���̽��� �־����Ƿ�, ������ ó���մϴ�.
	*/
	for (test_case = 1; test_case <= T; ++test_case)
	{
		int a, b;
		cin >> a >> b;
		int* arr = new int[b];
		vector<string> str;
		for (int i = 0; i < a; i++) {
			for (int x = 0; x < b; x++) {
				char t;
				cin >> t;
				arr[x] = t;
			}
			for (int x = 0; x < b; x++) {
				if (arr[x]!=48) {
					string temp = "";
					while (arr[x]!=48) {
						temp.push_back(arr[x]);
						x++;
						if (arr[x] == 48 && temp.size() < 14) {
							while(arr[x]!=4)
						}
					}
					int k = 1;
					for (int r=0; r < str.size(); r++) {
						if (temp.compare(str[r]) == 0) {
							k = 0;
							break;
						}
					}
					if (k == 1) {
						str.push_back(temp);
					}
				}
			}
		}
		int i;
		for (i = 0; i < str.size(); i++) {
			cout << str[i] << endl;
		}
		/*int code[8] = { 0, };
		int num1 = 0, num2 = 0;
		for (int j = 0; j <8; j++) {
			for (int a = 0; a < 7; a++) {
				code[j] += (temp[i--]) * pow(a);
			}
			switch (code[j])
			{
			case 13:code[j] = 0;
				break;
			case 25:code[j] = 1;
				break;
			case 19:code[j] = 2;
				break;
			case 61:code[j] = 3;
				break;
			case 35:code[j] = 4;
				break;
			case 49:code[j] = 5;
				break;
			case 47:code[j] = 6;
				break;
			case 59:code[j] = 7;
				break;
			case 55:code[j] = 8;
				break;
			case 11:code[j] = 9;
				break;
			default:
				break;
			}
			if (j > 0 && j % 2 == 1) {
				num1 += code[j];
			}
			if (j > 0 && j % 2 == 0) {
				num2 += code[j];
			}
		}
		if ((num1 * 3 + num2 + code[0]) % 10 == 0) {
			cout << "#" << test_case << " " << num1 + num2 +code[0]<< endl;
		}
		else {
			cout << "#" << test_case << " " << "0" << endl;
		}
		*/
	}
	return 0;//��������� �ݵ�� 0�� �����ؾ��մϴ�.
}