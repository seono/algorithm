#include<cstdio>
#include<cstdlib>

int block_length = 0;
int wall_length = 0;

char* block;
char* wall;

int answer_num = 0;
int answer_height = 0;
char blocks[1000][200] = { 0, };

int addblocks(int idx, int i, int st) {
	for (int a = 0; a < block_length; a++) {
		if (blocks[a + i][st] != 0)return 0;
	}
	for (int a = idx; a < block_length; a++) {
		blocks[a + i][st] = 1;
	}
	return 1;
}

void calculator() {
	int L = 0, R = 0;
	int st = 100;
	int m_st = 100, h_st = 100;
	for (int i = 0; i < wall_length;) {
		//���� ���� ���ڰ� ���� ��� == ������ �׾ƾ� �ϴ� ���
		if (wall[i] == block[0]) {
			//����߰�
			answer_num++;
			//addblock�Լ��� i=�ε���, st= ��
			//�ε����� �������� �ش� ������ ��� �ֱ�ȵǸ� 0��ȯ
			//�����ϸ� �ְ� 1��ȯ
			while (addblocks(0, i, st) == 0) {
				st++;
			}
			//�׾ƿø� ���� ���� ���� ������ ��
			h_st = st > h_st ? st : h_st;
			int tmp = 0;
			//������ �ε������� ���� ��� �˻� �Ѿ
			while (wall[i] == block[tmp]) {
				i++;
				tmp++;
			}
		}//��� ���� ���� ������ �ٸ� ���� ���� ���==�ؿ��ٳ־���ϴ°��
		else {
			answer_num++;
			//��Ͽ��� �ش� ������ ���ڰ� ���° ���� Ž��
			for (int idx = 1; idx < block_length; idx++) {
				if (wall[i] == block[idx]) {
					//��� ���� ���ʺ��� ä���� ������
					//���� ���̴� ���ڿ����� ���������� ä�������� �������.
					while (addblocks(idx, i - idx, st) == 0) {
						st--;
					}
					//���� ���� ������ ��
					m_st = st < m_st ? st : m_st;
					int tmp = idx;
					while (wall[i] == block[tmp]) {
						i++;
						tmp++;
					}
					break;
				}
			}
		}
	}
	answer_height = h_st - m_st+1;
}

int main() {
	scanf("%d", &block_length);
	scanf("%d", &wall_length);

	block = (char*)malloc(sizeof(char) * (block_length + 1));
	wall = (char*)malloc(sizeof(char) * (wall_length + 1));

	scanf("%s", block);
	scanf("%s", wall);
	
	calculator();

	printf("%d\n", answer_num);
	printf("%d\n", answer_height);

	return 0;
}