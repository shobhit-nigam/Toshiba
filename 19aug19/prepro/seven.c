#include<stdio.h>
#include"chocolate.h"
#undef Z
#define Z 100
const int phone = 22;
void main()
	{
	int ma = 10;
	int gc = 0;
	#if Y == 100
	printf("we all go home at 6:10\n");
	printf("we all come tom at 8:10\n");
	#elif Y < 100
	printf("we all go home at 7:10\n");
	printf("we all come tom at 8:15\n");
	#else
	printf("we all come to class on weekends\n");
	printf("we all come tom at 8:10\n");
	#endif
	}
