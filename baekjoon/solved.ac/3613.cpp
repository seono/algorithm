#include<iostream>
using namespace std;

int main() {
	string str;
	cin >> str;
	bool iscplus = false;
	//�ҹ��� ����
	if (str[0] < 97 || str[0]>122) {
		cout << "Error!";
		return 0;
	}
	//_������
	if (str[str.size() - 1] == 95) {
		cout << "Error!";
		return 0;
	}
	for (unsigned int i = 1; i < str.size(); i++) {
		char a = str[i];
		if (a == 95)iscplus = true;
		//__����
		if (i < str.size() - 2 && a == 95 && str[i + 1] == 95) {
			cout << "Error!";
			return 0;
		}
	}
	if (iscplus) {
		for (unsigned int i = 0; i < str.size(); i++) {
			char a = str[i];
			//�ҹ��ھƴѰ�
			if (a != 95 && (a < 97 || a>122)) {
				cout << "Error!";
				return 0;
			}
			if (a == 95) {
				if (str[i + 1] < 91) {
					cout << "Error!";
					return 0;
				}
				str[i + 1] -= 32;
				str.erase(str.begin() + i);
			}
		}
	}
	else {
		for (unsigned int i = 0; i < str.size(); i++) {
			char a = str[i];
			if (a < 91) {
				str[i] += 32;
				str.insert(i, "_");
			}
		}
	}
	cout << str;
	return 0;
}