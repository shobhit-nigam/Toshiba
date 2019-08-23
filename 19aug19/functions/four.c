#include<stdio.h>
void funca();
void main()
	{
	int ma=20;
//	register int mb = 30;
	printf("mb=%d adr=%u\n", mb,&mb);
	funca();
	funca();
	funca();
	return;
	}
void funca()
	{	
	int lc = 0;
//	printf("la=%d adr=%u\n", la, &la);
//	printf("lb=%d adr=%u\n", lb, &lb);
	}

