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
	// List 1
	struct ListNode* l1 = createNode(1);


	if(l1 != NULL){
		l1->next = createNode(3);
		l1->next->next = createNode(8);
		// printf("%d", l1->next->next->val);
	}

	// List 2
	struct ListNode* l2 = createNode(1);

	// TODO: Start working with currentListNode

	if(l2 != NULL){
		l2->next = createNode(3);
		l2->next->next = createNode(18);
		printf("%d", l2->next->next->val);
	}


	// TODO: Start working with currentListNode

	return 0;
}
