#include<stdio.h>
#include<unistd.h>
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
	for (i=9; i>0; i--)
	{
		printf("main will finish in %d secs\n", i);
		sleep(1);
	}
	taska();
	taskb();
	return;
}
