
void print(char* val){
	printf("--> %s\n", val);
}

int stringLength(char *s){
	if(s == NULL){
		return 0;
	}

	int length = 0;

	while(s[length] != '\0'){
		length += 1;
	}

	return length;
}
