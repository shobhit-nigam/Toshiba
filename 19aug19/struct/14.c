#include<stdio.h>

struct motor 
{
	int ia;
	int ib;
}pump;

struct dcmotor 
{
	int ic;
	int id;
	struct motor induct;
}dcpump;

struct engine
{
	int ie;
	int ig;
	struct motor brush;
	struct dcmotor dbrush;
}epump;

void main()
{
	int varx = 3;	
	struct motor step;

}







