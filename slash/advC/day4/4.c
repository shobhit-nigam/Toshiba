#include<stdio.h>

void main()
{
	volatile int varx = 30, vary = 20, varz = 100;
	int vara = 0, varb = 110;
	vara = varx + vary * varz;
	varb = varx+2 + vary*3 + varz*4;

	varb = ++varx;
	// varx = varx + 1;
	// varb = varx
	return;
}

