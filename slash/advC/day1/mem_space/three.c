#include<stdio.h>
void funca(int, int);
int ga = 100;
int gb = 200;


void main(){
	int ma = 10, mb = 12;
	printf("ma=%d adr=%u\n", ma, &ma);
	printf("mb=%d adr=%u\n", mb, &mb);
	printf("ga=%d adr=%u\n", ga, &ga);
	printf("gb=%d adr=%u\n", gb, &gb);
	funca(100, 200);
	return;
}

void funca(int la, int lb){
	printf("la=%d adr=%u\n", la, &la);
	printf("lb=%d adr=%u\n", lb, &lb);
	return;
}
