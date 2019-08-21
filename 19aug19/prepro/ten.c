#include<stdio.h>
#include<unistd.h>
void main()
{
	int i=0;
	for(i=6; i>=0; i--)
	{
		printf("will end in %d\n", i);
		sleep(1);
	}

}
