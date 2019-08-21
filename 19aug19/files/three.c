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
	fdb = open("thanos", O_WRONLY);
	printf("groot's fd=%d\n",fda); 
	printf("thanos' fd=%d\n",fdb); 
	read(fda, buf, 10);
	printf("read data is %s\n", buf);
	write(fdb, buf, 7);
	printf("written\n");
	return;
}
