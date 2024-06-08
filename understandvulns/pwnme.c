#include <stdio.h>
#include <string.h>

// compile with 
// gcc -i bufflow pwnme.c
int main() {
    char buffer[10]; // A buffer with a fixed size of 10 bytes
    int specialval = 1;
    printf("Enter some text: ");
    gets(buffer); 


    printf("You entered: %s\n", buffer);
    if (specialval != 1) {
    	secretfunction();
    }
    return 0;
}


int secretfunction() {
	printf("Congrats! You have found the secret function!\n\n");
	return 0;
}
