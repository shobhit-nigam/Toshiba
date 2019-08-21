#include<stdio.h>

typedef struct 
{
	int ia;
	short int ib;
	char ca;
}motor;

void main()
{
	int varx = 3;	
	typedef int salary;
	salary vara = 101;
	int varb;
	motor step;
	motor pump;
//	pump step;
	step.ia = 360;		//00000000 00000000 00000001 01101000
	printf("step.ia=%d\n", step.ia);
	printf("step.ca=%c\n", step.ca);
	step.ca = 'A';
	printf("step.ia=%d\n", step.ia);
	printf("step.ca=%c\n", step.ca);

}







