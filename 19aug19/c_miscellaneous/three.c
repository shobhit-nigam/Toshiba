#include<stdio.h>
void funca()
{
	printf("in func a\n");
}

void main()
{
	void (*f)(void);
	void (*r[2]) (void);
	f = funca;
	r[0] = funca;
	f();
	r[0]();
//	funca();

}
