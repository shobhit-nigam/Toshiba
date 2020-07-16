#include<stdio.h>
void funca(int, int);
void funcb(int, int);
int ga = 100;
int gb = 200;


void main(){
	int ma = 10, mb = 12;
	printf("ma=%d adr=%u\n", ma, &ma);
	printf("mb=%d adr=%u\n", mb, &mb);
	funca(22, 23);
	funcb(70, 80);
	printf("ga=%d adr=%u\n", ga, &ga);
	printf("gb=%d adr=%u\n", gb, &gb);
	return;
}

void funca(int la, int lb){
	int lc = 24;
	printf("-------starting A--------\n");
	printf("la=%d adr=%u\n", la, &la);
	printf("lb=%d adr=%u\n", lb, &lb);
	printf("lc=%d adr=%u\n", lc, &lc);
	funcb(100, 200);
	printf("-------ending A---------\n");
	return;
}

void funcb(int ta, int tb){
	int tc = 300;
	printf("-------starting B--------\n");
	printf("ta=%d adr=%u\n", ta, &ta);
	printf("tb=%d adr=%u\n", tb, &tb);
	printf("tc=%d adr=%u\n", tc, &tc);
	printf("-------ending B---------\n");
	return;
}
