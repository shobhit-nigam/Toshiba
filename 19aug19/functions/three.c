#include<stdio.h>
//prototype	called		definition
void funca(int, int);
void funcb(int, int);
void main()
	{
	int ma=20, mb=30;
	printf("ma=%d adr=%u\n", ma, &ma);
	printf("mb=%d adr=%u\n", mb, &mb);
	funca(ma, mb);
	funcb(100, 200);
	return;
	}
void funca(int la, int lb)
	{	
	int lc = 0;
	printf("starting func A\n");
	printf("la=%d adr=%u\n", la, &la);
	printf("lb=%d adr=%u\n", lb, &lb);
	funcb(-20, -30);
	printf("lc=%d adr=%u\n", lc, &lc);
	printf("ending func A\n");
	return ;
	}
void funcb(int ta, int tb)
	{	
	int tc = 0;
	printf("starting func B\n");
	printf("ta=%d adr=%u\n", ta, &ta);
	printf("tb=%d adr=%u\n", tb, &tb);
	printf("tc=%d adr=%u\n", tc, &tc);
	printf("ending func B\n");
	return ;
	}

