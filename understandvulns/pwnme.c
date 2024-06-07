#include <stdio.h>
#include <string.h>


//compile with gcc -o bufflow pwnme.c -no-pie
int main() {
    char buffer[10]; // A buffer with a fixed size of 10 bytes

    printf("Enter some text: ");
    gets(buffer); 


    printf("You entered: %s\n", buffer);

    return 0;
}


int secretfunction() {
	printf("Congrats! You have found the secret function!\n\n");
	return 0;
}
