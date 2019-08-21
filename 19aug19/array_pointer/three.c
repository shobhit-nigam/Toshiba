#include<stdio.h>

void main()
	{
	int ar[5] = {6,3,12,9,17};
	int *br[5]; 
	int *p;
	int i=0;
	printf("ar=%u, *ar=%d\n", ar, *ar);
	p = ar;
	for(i=0; i<5; i++)
		{
		br[i] = &ar[i];
		}
	printf("br=%u, *br=%u **br=%d\n", br, *br, **br);
	printf("br[2]=%u, *br[2]=%d\n", br[2], *br[2]);
	}

