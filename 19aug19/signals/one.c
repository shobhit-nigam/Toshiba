#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
void main()
{
	int i=0;
	for(i=0; 1; i++)
		{
		printf("running since %d seconds\n", i);
		sleep(1);
		}
}
