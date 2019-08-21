#include<stdio.h>

union motor 
{
	int ia;
	short int ib;
	char ca;
}pump;

void main()
{
	int varx = 3;	
	union motor step;
	step.ia = 360;		//00000000 00000000 00000001 01101000
	printf("step.ia=%d\n", step.ia);
	printf("step.ca=%c\n", step.ca);
	step.ca = 'A';
	printf("step.ia=%d\n", step.ia);
	printf("step.ca=%c\n", step.ca);

}







