#include<stdio.h>
#include"app.h"
extern int funca();
extern int funcb();
extern int funcc();

void main()
{
	int ma=0, mb=0, mc=0;
	int tot=0;
	ma=funca();
	mb=funca();
	mc=funca();
	tot=ma+mb+mc+MAX;
	printf("tot=%d\n", tot);
	return;
}

