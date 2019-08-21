#include<stdio.h>

struct motor 
{
	int rpm;
	int ia;
	struct motor induct;
}pump;

struct dcmotor 
{
	int rpm;
	int ia;
}dcpump;


void main()
{
	int varx = 3;	
	struct motor step;
//	pump = dcpump;
//	printf("sizeof step=%d\n", sizeof(step));

}







