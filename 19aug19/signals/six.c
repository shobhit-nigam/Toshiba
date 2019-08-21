#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
void main()
{
	int i=0, pid;
	pid = getpid();
	alarm(10);
	for(i=0; 1; i++)
		{
		printf("%d running since %d seconds\n", pid,i);
		sleep(1);
		}
}
