#include<stdio.h>
#include<unistd.h>

void main(){
	int i = 0;
	for (i=0; 1 ; i++)
	{
		printf("i=%d\n", i);
		sleep(1);
	}
	return;
}
