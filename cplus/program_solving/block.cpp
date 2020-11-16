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
		//가장 왼쪽 문자가 나온 경우 == 위에다 쌓아야 하는 경우
		if (wall[i] == block[0]) {
			//블록추가
			answer_num++;
			//addblock함수는 i=인덱스, st= 층
			//인덱스는 고정으로 해당 층에서 블록 넣기안되면 0반환
			//가능하면 넣고 1반환
			while (addblocks(0, i, st) == 0) {
				st++;
			}
			//쌓아올린 층이 가장 높은 층인지 비교
			h_st = st > h_st ? st : h_st;
			int tmp = 0;
			//성벽의 인덱스에서 같은 블록 검사 넘어감
			while (wall[i] == block[tmp]) {
				i++;
				tmp++;
			}
		}//블록 가장 왼쪽 제외한 다른 문자 나온 경우==밑에다넣어야하는경우
		else {
			answer_num++;
			//블록에서 해당 성벽의 문자가 몇번째 인지 탐색
			for (int idx = 1; idx < block_length; idx++) {
				if (wall[i] == block[idx]) {
					//블록 가장 왼쪽부터 채워도 되지만
					//눈에 보이는 문자열부터 오른쪽으로 채워나가도 상관없다.
					while (addblocks(idx, i - idx, st) == 0) {
						st--;
					}
					//가장 낮은 층인지 비교
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