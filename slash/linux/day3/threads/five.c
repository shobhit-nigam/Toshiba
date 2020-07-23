#include<stdio.h>
#include<unistd.h>
#include<pthread.h>
#include<stdlib.h>
int data = 0;
void taska()
{
	int i = 0;
	for (i=3; i>0; i--)
	{
		data = data + i;
		printf("data = %d\n", data);
		sleep(2);
	}
	return;
}

void taskb()
{
	int i = 0;
	for (i=7; i>0; i--)
	{
		data = data + data*i;
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
	pthread_join(ta, NULL);
	pthread_join(tb, NULL);
	return;
}
