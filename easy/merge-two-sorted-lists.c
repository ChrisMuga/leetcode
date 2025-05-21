#include <stdio.h>
#include <stdlib.h>

// Definition for singly-linked list.
struct ListNode {
	int val;
	struct ListNode *next;
};

// struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
// 	struct ListNode* res = { 4, NULL }; 
//
// 	return res;
// }

struct ListNode* createNode(int val){
	struct ListNode* res = (struct ListNode*)(malloc(sizeof(struct ListNode)));

	if(res != NULL){
		res->val = val;
		res->next = NULL;
	}

	return res;
}

int main(){
	struct ListNode* test = createNode(1);

	// TODO: Start working with currentListNode

	if(test != NULL){
		test->next = createNode(3);
		printf("%d", test->next->val);
	}

	return 0;
}
