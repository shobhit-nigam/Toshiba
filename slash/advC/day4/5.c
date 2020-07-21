#include<stdio.h>

double funca(double data, unsigned int n)
{
	volatile double varx = 1;
	unsigned i = 0;
	for (i =1; i<=n; i++){
		varx = varx *data;
	}
	return varx;
}

void main()
{
	volatile double vary = 195689;
	volatile double varx = 789324;
	double varz = 0;
	unsigned int i = 0, j=0;
	for (j=0; j<=10000000; j++){

		for (i=0; i<=10000000; i++){
			varz = vary*j + varx*i;
		}
	}
	return;
}
