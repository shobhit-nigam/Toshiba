#include<stdio.h>
#include<unistd.h>
#include<fcntl.h>
void main()
{
	int fda=0, fdb=0;
	int pid=0;
	static char buf[20];
	pid = getpid();
	printf("groot's fd=%d\n",fda); 
	printf("thanos' fd=%d\n",fdb); 
	read(0, buf, 6);
	write(1, buf, 5);
	return;
}
