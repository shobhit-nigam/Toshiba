#include<stdio.h>
#include<unistd.h>

void main()
{
	int pid=0;
	int i=0;
	pid = getpid();
	for (i=0; 10 ; i++)
	{
		printf("%d running since %d secs\n", pid, i);
		sleep(1);
	}
	return;
}
