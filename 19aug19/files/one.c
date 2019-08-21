#include<stdio.h>
#include<unistd.h>
#include<fcntl.h>
void main()
{
	int fda=0, fdb=0;
	int pid=0;
	pid = getpid();
	fda = open("groot", O_RDONLY);
	perror("");
	printf("groot's fd=%d\n",fda); 
	return;
}
