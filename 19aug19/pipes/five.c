#include<stdio.h>
#include<fcntl.h>
#include<unistd.h>

void main()
{
	int fda;
	static char buf[20];
	printf("opening a file\n");
	fda = open("shaktiman", O_WRONLY);
	printf("going to write\n");
	write(fda, "sorry shaktiman", 15);
	printf("written\n");
	return;
}
