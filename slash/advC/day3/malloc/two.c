#include<stdio.h>
#include<stdlib.h>

void main()
{
	int ar[5];
	int n=0, i=0;
	int *ptr;

	printf("enter the size\n");
	scanf("%d", &n);
	// array of pointers
	ptr = (int *)malloc(n * sizeof(int *));
	
	
	free(ptr);
	printf("\n");
	return;
}
