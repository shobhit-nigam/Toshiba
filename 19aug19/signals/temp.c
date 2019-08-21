#include<stdio.h>
#include<signal.h>
#include<unistd.h>
void funca()
{
	printf("signal handled, no big deal\n");
	return;
}
void funcb()
{
	int i=0;
	printf("talk to my hand\n");
	for(i=10; i>0; i--)
	{
		printf("in the handler for %d secs\n", i);
		sleep(1);
	}
	return;
}
void main()
{
	int i=0, pid;
	pid = getpid();
	signal(SIGTERM, funca);
	signal(SIGINT, funcb);
//	signal(SIGKILL, funcb);
	for(i=0; 1; i++)
		{
		printf("%d running since %d seconds\n", pid,i);
		sleep(1);
		}
}
