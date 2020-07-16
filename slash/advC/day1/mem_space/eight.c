#include<stdio.h>

void funca();
int g;
static int h = 10;

void main(){
	funca();
	return;
}

void funca(){
	int i;
	static int j;
	printf("----in A----\n");
	printf("g=%d adr=%u\n", g, &g);
	printf("i=%d adr=%u\n", i, &i);
	printf("j=%d adr=%u\n", j, &j);
	return;
}
