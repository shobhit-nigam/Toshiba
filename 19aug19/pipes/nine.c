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
	printf("written once\n");
	sleep(5);
	write(fda, "andhera kayam rahe", 18);
	sleep(5);
	return;
}
