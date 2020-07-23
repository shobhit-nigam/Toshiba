#include<stdio.h>
#include<unistd.h>
#include<pthread.h>
#include<stdlib.h>
pthread_mutex_t flag; 
int data = 0;
void taska()
{
	int i = 0;
	printf("A wants the mutex\n");
	pthread_mutex_lock(&flag);
	printf("A has taken the mutex\n");
	for (i=3; i>0; i--)
	{
		data = data + i;
		printf("data = %d\n", data);
		sleep(2);
	}
	printf("A releases the mutex\n");
	pthread_mutex_unlock(&flag);
	return;
}

void taskb()
{
	int i = 0;
	printf("B wants the mutex\n");
	pthread_mutex_lock(&flag);
	printf("B has taken the mutex\n");
	for (i=7; i>0; i--)
	{
		data = data + data*i;
		sleep(1);
	}
	printf("B releases the mutex\n");
	pthread_mutex_unlock(&flag);
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
