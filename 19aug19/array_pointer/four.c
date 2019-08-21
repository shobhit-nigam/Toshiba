#include<stdio.h>

void main()
	{
	int ar[5] = {6,3,12,9,17};
	int *br[5]; 
	int *p, **q;
	int i=0;
	int varu=0, varv=0, varw=0, varx=0, vary=0;
	printf("ar=%u, *ar=%d\n", ar, *ar);
	p = ar;
	q = br;
	for(i=0; i<5; i++)
		{
		br[i] = &ar[i];
		}
	varu = *p***q;
	varv = *++p + **++q;
	varw = ++*p + ++**q;
	varx = *p++ + **q++;
	vary = ++*p++-++**q++;
	printf("varu=%d\nvarv=%d\nvarw=%d\n", varu, varv, varw);
	printf("varx=%d\nvary=%d\n", varx, vary);
	printf("*p=%d, **q=%d\n", *p, **q);
	}

