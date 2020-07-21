#include<stdio.h>
#include<unistd.h>
#include<signal.h>

void funca(){
	printf("handles the signal, no big deal\n");
	return;
}

void funcb(){
	printf("talk to my hand\n");
	return;
}

void main()
{
	int pid=0;
	int i=0;
	signal(SIGTERM, funca);
	signal(SIGINT, funcb);
	signal(SIGKILL, funcb);
	pid = getpid();
	for (i=0; 10 ; i++)
	{
		printf("%d running since %d secs\n", pid, i);
		sleep(1);
	}
	return;
}
