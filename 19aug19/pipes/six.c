#include<stdio.h>
#include<fcntl.h>
#include<unistd.h>

void main()
{
	int fda;
	static char buf[20];
	printf("opening a file\n");
	fda = open("shaktiman", O_RDONLY);
	printf("going to read\n");
	read(fda, buf, 7);
	printf("read data is %s\n", buf);
	return;
}
