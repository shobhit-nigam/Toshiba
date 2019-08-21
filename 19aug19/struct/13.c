#include<stdio.h>

struct motor 
{
	int rpm;
	int ia;
	struct motor *ptr;
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
	pump.ptr = &step;	//motor ptr
	pump.ptr->rpm;		//int
	pump.ptr->ptr;		//motor ptr
	pump.ptr->ptr = &step;
	pump.ptr->ptr->rpm;	//int
	
	step.ptr = &step;
//	pump = dcpump;
//	printf("sizeof step=%d\n", sizeof(step));

}







