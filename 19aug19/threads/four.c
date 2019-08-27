#include<stdio.h>
#include<pthread.h>
#include<unistd.h>
void funca()
{
	int i=0;
	for(i=9; i>0; i--)
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
	pthread_t ta, tb;
	pthread_create(&ta, NULL, (void *)funca, NULL);
	pthread_create(&tb, NULL, (void *)funcb, NULL);
		
	for(i=6; i>0; i--)
	{
		printf("%d secs left in main\n",i);
		sleep(1);
	}
	pthread_join(ta, NULL);
	pthread_join(tb, NULL);
	printf("last line of main\n");
	return;
}
















