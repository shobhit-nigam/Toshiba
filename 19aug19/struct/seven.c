#include<stdio.h>

struct motor 
{
	int rpm;
	int torque;
	int *p;
}pump;

struct motor brushl;

void main()
{
	int varx = 3;	
	struct motor step;
	struct motor induct;
	step.rpm = varx;		//int
	step.torque = 44;		//int
	step.p = &varx;			//int pointer
	pump = step;
	printf("pump.torque=%d adr=%u\n", pump.torque, &pump.torque);
	printf("pump.rpm=%d adr=%u\n", pump.rpm, &pump.rpm);
	printf("step.p=%u *step.p=%d\n", step.p, *step.p);

}

