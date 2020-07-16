#include<stdio.h>
void funca();
int g = 9;
static int h = 10;

void main(){
	funca();
	funca();
	funca();
	return;
}

void funca(){
	int i=0;
	static int j=0;
	++i;	++j;
	printf("----in A----\n");
	printf("g=%d adr=%u\n", g, &g);
	printf("i=%d adr=%u\n", i, &i);
	printf("j=%d adr=%u\n", j, &j);
	return;
}
