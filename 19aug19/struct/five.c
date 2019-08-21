#include<stdio.h>

struct motor 
{
	int rpm;
	int torque;
}pump;
struct motor brushl;

void main()
{
	int varx = 3;	
	struct motor step = {56, 78};
	struct motor induct;
	step.rpm = varx;
	pump = step;
	printf("pump.torque=%d adr=%u\n", pump.torque, &pump.torque);
	printf("pump.rpm=%d adr=%u\n", pump.rpm, &pump.rpm);
	printf("pump=%d adr=%u\n", pump, &pump);
	
}
