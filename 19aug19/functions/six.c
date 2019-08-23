#include<stdio.h>
void funca();
int ga = 10;
extern int gb;
void main()
	{
	int ma;
	ma = ga + gb + ma;
	printf("ma=%d\n", ma);
	return;
	}
void funca()
	{	
	}

