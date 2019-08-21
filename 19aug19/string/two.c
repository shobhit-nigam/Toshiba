#include<stdio.h>

void main()
{
	char ar[6] = {'h', 'e', 'l', 'l', 'o', '\0'};
	char br[6] = {104, 101, 108, 108, 111, 0};
	char cr[6] = "hello";
	char *dr = "hello";
	char *er;
	char fr[6] = {*dr, *(dr+1), *(dr+2)};
//	char fr[6] = dr;
	er = dr;
	printf("dr=%s adr=%u\n", dr, dr);
	printf("er=%s adr=%u\n", er, er);
	dr = "world";
	printf("dr=%s adr=%u\n", dr, dr);
	printf("er=%s adr=%u\n", er, er);
	return;
}
