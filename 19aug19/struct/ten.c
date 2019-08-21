#include<stdio.h>

struct motor 
{
	int rpm;
	int torque;
	int *p;
	char sound[10];
}pump, *ptr;

void main()
{
	int varx = 3;	
	struct motor step;
	struct motor induct = {55, 66, &varx, "vroom"};
	struct motor arr[3];
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
	arr[0] = induct;	
	arr[0];				//motor
	arr[0].rpm; 			//int
	arr[0].p;			//int pointer
	*arr[0].p;			//int
	arr->sound;			//char const pointer
	*arr->sound;			//char 

	pump = step;
	printf("arr[0].sound[0]=%c\n", arr[0].sound[0]);
	printf("*arr->sound=%c\n", *arr->sound);
	printf("arr->sound=%s\n", arr->sound);

}







