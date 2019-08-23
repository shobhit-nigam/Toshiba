#include<stdio.h>
void funca();
void main()
	{
	funca();
	funca();
	funca();
	return;
	}
void funca()
	{	
	int la = 0;
	static int lb = 0;
	++la;	++lb;
	printf("la=%d adr=%u\n", la, &la);
	printf("lb=%d adr=%u\n", lb, &lb);
	}

