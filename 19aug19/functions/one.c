#include<stdio.h>
//prototype	called		definition
void funca(int, int);
int ga = 12;
void main()
	{
	int ma=20, mb=30;
	printf("ma=%d adr=%u\n", ma, &ma);
	printf("mb=%d adr=%u\n", mb, &mb);
	printf("ga=%d adr=%u\n", ga, &ga);
	funca(ma, mb);
	return;
	}
void funca(int la, int lb)
	{	
	int lc = 0;
	printf("la=%d adr=%u\n", la, &la);
	printf("lb=%d adr=%u\n", lb, &lb);
	printf("lc=%d adr=%u\n", lc, &lc);
	return ;
	}


