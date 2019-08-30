#include<stdio.h>
#include<pthread.h>
#include<unistd.h>
pthread_t ta, tb;
int task = 0;

void func1()
{
	task =task + 1;
	printf("task%d has started\n", task);
	sleep(5);
	printf("task%d has finished\n", task);
}
void func2()
{
	task =task + 1;
	printf("task%d has started\n", task);
	sleep(5);
	printf("task%d has finished\n", task);
}

void main()
{
	pthread_create(&ta, NULL, (void *) func1, NULL);
	pthread_create(&tb, NULL, (void *) func2, NULL);
	pthread_join(ta, NULL);
	pthread_join(tb, NULL);
	printf("main will exit\n");
	return;
}












