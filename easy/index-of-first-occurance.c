/**
 * Find the Index of the First Occurrence in a String
 * difficulty: easy
 * https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
 **/

#include <stdio.h>
#include "helpers.h"


int strStr(char* haystack, char* needle) {
	// Get the length of the needle
	int lN = stringLength(needle);
	int lH = stringLength(haystack);

	if(lN > lH){
		return -1;
	}

	int x = 0;


	while(x < lH){
		char starter = haystack[x];

		int match = 0;
		if(starter == needle[0]){
			int i = 0;

			while(i < lN){
				if(needle[i] == haystack[x + i]){
					match += 1;
				}

				if(match == lN){
					return x;
				}
				i += 1;
			}
		}

		
		x += 1;
	}

	return -1;
}

int main(){
	int x = strStr("mississippi", "issipi");
	printf("%d\n", x);
	return 0;
}
