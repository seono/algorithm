#include<iostream>
#pragma warning(disable:4996)
using namespace std;
int ladd[100][100];

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
	T = 10;
	/*
	   ���� ���� �׽�Ʈ ���̽��� �־����Ƿ�, ������ ó���մϴ�.
	*/
	for (test_case = 1; test_case <= T; ++test_case)
	{
		cin >> test_case;
		for (int a = 0; a < 99; a++) {
			for (int b = 0; b < 100; b++) {
				cin >> ladd[a][b];
			}
		}
		int start;
		for (int a = 0; a < 100; a++) {
			cin >> ladd[99][a];
			if (ladd[99][a] == 2) {
				start = a;
			}
		}
		for (int a = 1; a < 100; a++) {
			if (start<99&&ladd[99 - a][start + 1] == 1) {
				while (start < 99 && ladd[99 - a][start+1]) {
					ladd[99 - a][start]++;
					start++;
				}
				continue;
			}
			else if (start>0&&ladd[99 - a][start - 1] == 1) {
				while (start > 0 && ladd[99 - a][start-1]) {
					ladd[99 - a][start]++;
					start--;
				}
				continue;
			}
			ladd[99 - a][start]++;
		}
		cout << "#" << test_case << " " << start << endl;
	}
	return 0;//��������� �ݵ�� 0�� �����ؾ��մϴ�.
}