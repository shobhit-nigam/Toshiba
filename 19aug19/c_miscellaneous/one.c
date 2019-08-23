#include<stdio.h>
void funca()
{
	printf("in func a\n");
}

void main()
{
	int (*f)(void);
	f = funca;
	f();
//	funca();

}
