#include<stdio.h>
void funca()
{
	printf("in func a\n");
}

void main()
{
	void (*f)(void);
	int (*r[2]) (void);
	f = funca;
	f(7, 8);
//	funca();

}
