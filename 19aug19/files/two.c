#include<stdio.h>
#include<unistd.h>
#include<fcntl.h>
void main()
{
	int fda=0, fdb=0;
	int pid=0;
	static char buf[20];
	pid = getpid();
	fda = open("groot", O_RDONLY);
	perror("");
	printf("groot's fd=%d\n",fda); 
	read(fda, buf, 6);
	printf("read data is %s\n", buf);
	read(fda, buf, 6);
	printf("read data is %s\n", buf);
	return;
}
