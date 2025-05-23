#include <stdio.h>
#include <stdlib.h>

// Definition for singly-linked list.
struct ListNode {
	int val;
	struct ListNode *next;
};

 struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
	printf("%d\n", list1->val);
	printf("%d\n", list2->next->next->val);
 	return list2;
}

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
	// [1 -> 3 -> 8]
	struct ListNode* l1 = createNode(1);


	if(l1 != NULL){
		l1->next = createNode(3);
		l1->next->next = createNode(8);
		// printf("%d", l1->next->next->val);
	}

	// List 2
	// [ 2 -> 7 -> 18]
	struct ListNode* l2 = createNode(2);

	// TODO: Start working with currentListNode

	if(l2 != NULL){
		l2->next = createNode(7);
		l2->next->next = createNode(18);
	}

	mergeTwoLists(l1, l2);


	// TODO: Start working with currentListNode
	// Expected result: [1 -> 2 -> 3 -> 7 -> 8 -> 18]

	return 0;
}
