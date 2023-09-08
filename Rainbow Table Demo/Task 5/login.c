# include <stdio.h>
# include <stdlib.h>
# include <string.h>

int main(int argc, char** argv){
    // Break the program if the password hasn't been supplied or the password length is larger than 6
    if(argc < 2){
        fprintf(stderr, "Bro, gimme your password to login.\n");
        fprintf(stderr, "Usage: ./login [your_password]\n");
        exit(1);
    }

    // Break the program if trying to login with password length larger than 6.
    if(strlen(argv[1]) > 7){
        exit(1);
    }

    // Security by obscurity: use binary operators to hide the actual password
    // If you wish: solve this task as "pwn" or "rev" ;)
    char* run = argv[0];
    char* passwd = argv[1];
    printf("Login password: %s", passwd);

    passwd[0] = passwd[0] >> 0x01;
    passwd[1] = 227 ^ passwd[0] + passwd[1];
    passwd[2] = passwd[strlen(passwd)-1] % 0x0A + passwd[2] + strlen(passwd) * 0x05;
    passwd[3] = 64 & 'A';
    passwd[4] = passwd[4] - run[2] + 67;
    int x = passwd[5];
    if(x==103){
        passwd[5] = 104;
    } else{
        passwd[5] = 0xed & 0x74;
    }

    // Check if the password is correct
    if(strcmp(passwd, "9Ns@Ph")==0){
        printf(" -- Congratulation! You are logged in as admin. Here is your spring roll :)\n");
    } else{
        printf(" -- I don't care if you are in my database or not, but you are not admin :-(\n");
    }
    return 0;
}
