/*
 * difficulty: easy
 * https://leetcode.com/problems/length-of-last-word/ 
*/

#include <stdio.h>

int stringLength(char* s){
	int length = 0;

	if(s == NULL){
		return 0;
	}

	while(s[length] != '\0'){
		length += 1;
	}

	return length;
}

int lengthOfLastWord(char* s) {
	// Get the length of the string
	int length = stringLength(s);

	int j = (length - 1);
	int i = (length - 1);

	// Find first letter
	while(i >= 0){
		if(s[i] != ' '){
			break;
		}
		i -= 1;
	}

	// Set j to the index of the first letter, if there are spaces at the end of the string
	if(i < j){
		j = i;
	}

	int count = 0;

	// Loop from the last index, until you run into " "
	while(j >= 0){
		if(s[j] != ' '){
			count += 1;
		}else if(s[j] == ' '){
			break;
		}
		j -= 1;
	}

	return count;
}

int main(){
	int ans = lengthOfLastWord("a ");

	printf("%d\n", ans);
}
