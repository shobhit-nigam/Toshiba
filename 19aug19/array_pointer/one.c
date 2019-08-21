#include<stdio.h>

void main()
	{
	int ar[5] = {6,3,12,9,17};
	int i=0;
	printf("ar=%u, *ar=%d\n", ar, *ar);
	for(i=0; i<5; i++)
		{
		printf("ar[%d] = %d[ar] = %d, adr=%u\n", i, i, ar[i], &ar[i]);
		}
	printf("ar[7] =%d\n", ar[7]);
	}

