#include <stdio.h>


int removeDuplicates(int* nums, int numsSize) {
	int i = 0;
	int j = i + 1;

	// Using 2 Pointer:
	// Given A and B, i.e nums[i] and nums[j]
	// Since the array is sorted:
	// If we find any mismatch, it means, we're at the tail end of a trail of duplicate.
	// Therefore, at that point, we can swap the current item at j, with the next item after i, i.e i+1
	// then increase i+1.
	// By the end of the loop, all the non-duplicates should be shored up to the top of the array. 
	// The order of the rest is irrelevant at that point.
	while(j < numsSize){
		if(nums[i] != nums[j]){
			nums[i + 1] = nums[j];
			i += 1;
		}

		j += 1;
	}

	return i + 1; 
}

int main() {
	printf("Yours is the world, and everything that's in it...\n");
	int val[10] = { 0, 0, 1, 1, 1, 2, 2, 3, 3, 4 };
	removeDuplicates(val, 10);
	return 0;
}
