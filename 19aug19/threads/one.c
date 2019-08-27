#include<stdio.h>
#include<pthread.h>
#include<unistd.h>
void funca()
{
	int i=0;
	for(i=6; i>0; i--)
	{
		printf("%d secs left in A\n",i);
		sleep(1);
	}
	return;
}
void funcb()
{
	int i=0;
	for(i=3; i>0; i--)
	{
		printf("%d secs left in B\n",i);
		sleep(1);
	}
	return;
}
void main()
{
	int i=0;
	funca();
	funcb();
	for(i=9; i>0; i--)
	{
		printf("%d secs left in main\n",i);
		sleep(1);
	}
	return;
}

