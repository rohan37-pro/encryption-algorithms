#include <stdio.h>
#include <ctype.h>


int main(){
	/*
	int ord = 65;
	char array[26];
	for (int i= 0; i<26; i++){
		array[i] = ord;
		ord++;
	}
	for (int i= 0; i<26; i++){
		printf("  %d\n",array[i]);
	}
	*/
	char array[500];
	char ch;
	int i=0;
	printf("enter string : ");
	scanf("%s",array);

	while (ch!='\0'){
		ch = array[i];
		array[i] = toupper(ch);
		i++;
	}
	printf("\nthe new string is %s",array);
}