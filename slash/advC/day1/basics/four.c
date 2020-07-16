#include<stdio.h>
#include<stdint.h>

void main()
{
	uint8_t data = 260;
	//0 to 255
	auto signed long int varx = 2;
	int vary = 3;
	long varz = 30;
	signed char x = 'x';
	printf("sizeof = %d\n", sizeof(data));
	printf("data = %d = %u\n", data, data);
}
