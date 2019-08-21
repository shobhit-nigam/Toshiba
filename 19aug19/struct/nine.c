#include<stdio.h>

struct motor 
{
	int rpm;
	int torque;
	int *p;
	char sound[10];
}pump, *ptr;

struct motor brushl;

void main()
{
	int varx = 3;	
	struct motor step;
	struct motor induct = {55, 66, &varx, "vroom"};
	step.rpm = varx;		//int
	step.torque = 44;		//int
	step.p = &varx;			//int pointer
	induct.sound;			//char const pointer
	induct.sound[2];		//char
	ptr;				//motor pointer
	ptr = &induct;			//ptr-> ==== induct.
	ptr->rpm;			//int
	ptr->p;		//induct.p	//int pointer
	*ptr->p;	//varx		//int
	pump = step;
	printf("pump.torque=%d adr=%u\n", pump.torque, &pump.torque);
	printf("pump.rpm=%d adr=%u\n", pump.rpm, &pump.rpm);
	printf("step.p=%u *step.p=%d\n", step.p, *step.p);

}







