#include<stdio.h>
//prototype	called		definition
void funca(int, int);
int ga = 12;
int gb = 13;
void main()
	{
	int ma=20, mb=30;
	printf("ma=%d adr=%u\n", ma, &ma);
	printf("ga=%d adr=%u\n", ga, &ga);
	printf("gb=%d adr=%u\n", gb, &gb);
	funca(++ma, ma++);
	printf("ma=%d adr=%u\n", ma, &ma);
	return;
	}
void funca(int la, int lb)
	{	
	int lc = 0;	int gb = 3;
	lc = la + lb + ++ga + ++gb;
	printf("la=%d adr=%u\n", la, &la);
	printf("lb=%d adr=%u\n", lb, &lb);
	printf("lc=%d adr=%u\n", lc, &lc);
	printf("ga=%d adr=%u\n", ga, &ga);
	printf("gb=%d adr=%u\n", gb, &gb);
	return ;
	}


