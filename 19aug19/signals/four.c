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
	printf("talk to my hand\n");
	return;
}
void main()
{
	int i=0, pid;
	pid = getpid();
	signal(SIGTERM, funca);
	signal(SIGINT, funcb);
	for(i=0; 1; i++)
		{
		printf("%d running since %d seconds\n", pid,i);
		sleep(1);
		}
}
