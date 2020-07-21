#include<stdio.h>

void abc_protocol(char *data){
	printf("working with data as per abc protocol\n");
	return;
}

void def_protocol(char *data){
	printf("working with data as per def protocol\n");
	return;
}

void geh_protocol(){
	printf("dataless protocol\n");
	return;
}

void main()
{
	void (*fptr)();
	fptr = geh_protocol;
	fptr();
		
	return;
}
