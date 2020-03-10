#include<iostream>

using namespace std;
typedef int Data;

int N, P;
int FG = 0;
typedef struct _Node {
	Data data;
	struct _Node* next;
}Node;

typedef struct _Stack {
	Node* head;
	Data len;
}Stack;
int isEmpty(Stack* stack) {
	return (stack->head == NULL);
}
void Push(Stack* stack, Data data) {
	Node* newNode = (Node*)malloc(sizeof(Node));
	newNode->data = data;
	newNode->next = stack->head;
	stack->head = newNode;
	FG++;
	return;
}
void Pop(Stack* stack) {
	if (!isEmpty(stack)) {
		Node* pop = stack->head;
		stack->head = pop->next;
		FG++;
		free(pop);
		return;
	}
	else return;
}
int Peek(Stack* stack) {
	return stack->head->data;
}

void Finger(Stack* stack, Data data) {
	if (isEmpty(stack) || Peek(stack) < data)Push(stack, data);
	else if (Peek(stack) == data) {
		return;
	}
	else {
		while (!isEmpty(stack) && Peek(stack) > data) {
			Pop(stack);
		}
		Finger(stack, data);
		return;
	}
}

int main() {
	Stack stack1; stack1.head = NULL;
	Stack stack2; stack2.head = NULL;
	Stack stack3; stack3.head = NULL;
	Stack stack4; stack4.head = NULL;
	Stack stack5; stack5.head = NULL;
	Stack stack6; stack6.head = NULL;

	cin >> N >> P;
	for (int i = 0, a, b; i < N; i++) {
		cin >> a >> b;
		switch (a)
		{
		case 1:Finger(&stack1, b); break;
		case 2:Finger(&stack2, b); break;
		case 3:Finger(&stack3, b); break;
		case 4:Finger(&stack4, b); break;
		case 5:Finger(&stack5, b); break;
		case 6:Finger(&stack6, b); break;
		default:
			break;
		}
	}
	cout << FG;
	return 0;
}