#include<stdio.h>
void funca();
extern void funcb();
int ga = 10;
extern int gb;
void main()
	{
	extern int ma;
	ma = ga + gb + ma;
	printf("ma=%d\n", ma);
	funcb();
	return;
	}
void funca()
	{	
	}

