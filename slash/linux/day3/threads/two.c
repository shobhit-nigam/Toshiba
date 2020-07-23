#include<stdio.h>
#include<unistd.h>
#include<pthread.h>
void taska()
{
	int i = 0;
	for (i=3; i>0; i--)
	{
		printf("task A will finish in %d secs\n", i);
		sleep(1);
	}
	return;
}

void taskb()
{
	int i = 0;
	for (i=6; i>0; i--)
	{
		printf("task B will finish in %d secs\n", i);
		sleep(1);
	}
	return;
}

void main()
{
	int i = 0;
	pthread_t ta, tb;
	pthread_create(&ta, NULL, (void *) taska, 0);
	pthread_create(&tb, NULL, (void *) taskb, 0);
	for (i=9; i>0; i--)
	{
		printf("main will finish in %d secs\n", i);
		sleep(1);
	}
	return;
}
