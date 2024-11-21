#include <stdio.h>
#include <ctype.h>

struct sockaddr_in {
    short sin_family;
    unsigned short sin_port;
    struct in_addr sin_addr;
    char sin_zero[8]; // Align
};

struct hostent {
    char *h_name; // domain name
    char **h_aliases; // other name
    int h_addrtype;
    int h_length;
    char **h_addr_list;
};

int main() {
    return 0;
}