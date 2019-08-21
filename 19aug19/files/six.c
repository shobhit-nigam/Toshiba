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
	printf("groot's fd=%d\n",fda); 
	close(1);
	fdb = open("thanos", O_WRONLY);
	printf("thanos' fd=%d\n",fdb); 
	printf("last line\n");
	return;
}
