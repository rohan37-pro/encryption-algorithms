#include <stdio.h>
#include <ctype.h>


char alphabets[26], refer_num[26];
int ord = 65;



int derefer_text(char text[], int array[]){
	char i;
	int msg_len=0 , index;
	while (text[msg_len]){
		i = text[msg_len];
		index = (int)i - 65;
		array[msg_len] = index;
		msg_len++;
	}
	return msg_len;
}


void uppercase(char *text){
	char ch;
	int i=0;

	while (text[i]){
		ch = text[i];
		text[i] = toupper(ch);
		i++;
	}
}


void encrypt(char plain_text[], char key[], char cipher[]){
	int msg2decimal[4096], key2decimal[30];
	uppercase(plain_text);
	uppercase(key);
	int text_len = derefer_text(plain_text, msg2decimal);
	int key_len = derefer_text(key, key2decimal);

	int i;
	for (i=0; i<text_len; i++){
		cipher[i] = alphabets[((msg2decimal[i] + key2decimal[i % (key_len)]) % 26)];
	}
	cipher[i+1] = '\0';
}



int main(){
	for (int i=0; i<26; i++){
		alphabets[i] = ord;
		refer_num[i] = i;
		ord++;
	}
	char choise;
	char msg[4096], key[30], cipher[4096];
	while (1){
		printf("choose- encrypt(e)/decrypt(d)/quit(q) : ");
		scanf("%c",&choise);
		if (choise=='Q' || choise=='q'){
			break;
		}
		if (choise=='e' || choise=='E'){
			printf("enter your message : ");
			scanf("%s",&msg);
			printf("key to encrypt : ");
			scanf("%s",&key);
			encrypt(msg, key, cipher);
			printf("cipher : %s\n\n",cipher);
		}
	}

	return 0;
}