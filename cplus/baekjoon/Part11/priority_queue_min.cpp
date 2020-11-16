#include<iostream>
#include<vector>
using namespace std;
#define MAX_E 200

typedef struct {
	int key;
}element;

typedef struct {
	element heap[MAX_E];
	int heap_size=0;
}HeapType;

void insert_min_heap(HeapType* h, element item) {
	int i;
	i = ++(h->heap_size);

	while ((i != 1) && (item.key < h->heap[i / 2].key)) {
		h->heap[i] = h->heap[i / 2];
		i /= 2;
	}
	h->heap[i] = item;
}

int delete_min_heap(HeapType* h) {
	if (h->heap_size == 0) return -1;
	element temp = h->heap[1];
	int i = 1;
	while (i*2<=h->heap_size) {
		if (h->heap[i * 2 + 1].key == NULL)h->heap[i] = h->heap[i * 2];
		else {
			if (h->heap[i * 2].key > h->heap[i * 2 + 1].key) {
				h->heap[i] = h->heap[i * 2];
				i = i * 2;
			}
			else {
				h->heap[i] = h->heap[i * 2 + 1];
				i = i * 2 + 1;
			}
		}
	}
	h->heap_size--;
	return temp.key;
}

void print_heap(HeapType* h, int idx) {
	if (idx > h->heap_size)return;
	else {
		cout << h->heap[idx].key << " ";
		print_heap(h, idx * 2);
		print_heap(h, idx * 2 + 1);
	}
	return;
}
int main() {
	HeapType heap1;
	element tmp;
	for (int i = 1; i < 10; i++) {
		tmp.key = i;
		insert_min_heap(&heap1, tmp);
	}
	print_heap(&heap1, 1);
	delete_min_heap(&heap1);
	print_heap(&heap1, 1);
	return 0;
}