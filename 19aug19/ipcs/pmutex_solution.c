#include<stdio.h>
#include<pthread.h>
#include<unistd.h>
pthread_t ta, tb;
int task = 0;
pthread_mutex_t flag;

void func1()
{
	printf("task A wants the mutex\n");
	pthread_mutex_lock(&flag);
	task =task + 1;
	printf("task%d has started\n", task);
	sleep(5);
	printf("task%d has finished, will release the lock\n", task);
	pthread_mutex_unlock(&flag);

}
void func2()
{
	printf("task B wants the mutex\n");
	pthread_mutex_lock(&flag);
	task =task + 1;
	printf("task%d has started\n", task);
	sleep(5);
	printf("task%d has finished, will release the lock\n", task);
	pthread_mutex_unlock(&flag);
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












