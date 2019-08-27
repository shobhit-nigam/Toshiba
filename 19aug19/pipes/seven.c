#include<stdio.h>
#include<fcntl.h>
#include<unistd.h>

void main()
{
	int fda;
	static char buf[20];
	printf("opening a file\n");
	sleep(3);
	fda = open("shaktiman", O_WRONLY);
	sleep(3);
	printf("going to write\n");
	sleep(3);
	write(fda, "sorry shaktiman", 15);
	sleep(50);
	printf("written\n");
	return;
}
