#include<stdio.h>

struct motor 
{
	int rpm;
	int torque;
	int *p;
}pump;

void funca(struct motor);
struct motor brushl;

void main()
{
	int varx = 3;	
	struct motor step;
	struct motor induct;
	step.rpm = varx;
	pump = step;
	printf("pump.torque=%d adr=%u\n", pump.torque, &pump.torque);
	printf("pump.rpm=%d adr=%u\n", pump.rpm, &pump.rpm);
	printf("pump=%d adr=%u\n", pump, &pump);
	funca(step);	
}
//	la = step
void funca(struct motor la)
{

}

