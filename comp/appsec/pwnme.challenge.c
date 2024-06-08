#include <stdio.h>
#include <string.h>

// compile with gcc -g -o bufflowchallenge pwnme.challenge.c -no-pie
int main() {
    char buffer[11]; // A buffer with a fixed size
    int protector = 0;
    long long int specialval = 7;
    printf("Enter some text: ");
    gets(buffer); 


    printf("You entered: %s\n", buffer);
    printf("value of specialval: 0x%lx 0x%x\n", specialval, protector);
    if (specialval == 0x6665656264616564 && protector == 0) {
    	secretfunction();
    } else {
    	printf("I don't have a gatekey\n");
    }
    return 0;
}


int secretfunction() {
	printf("Oh you mean this gatekey\nPCSC-BUFFER-BEEP \n\n");
	return 0;
}
