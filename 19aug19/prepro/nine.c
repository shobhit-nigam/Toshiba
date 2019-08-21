#include<stdio.h>
#define Y 100
#define Z 200
#define X 4+3
void funca();
void main()
	{
	int ma = 10;
	int gc = 0;
	#if Z == 100
	printf("we all go home at 6:10\n");
	printf("we all come tom at 8:10\n");
	#endif
	funca();
	#if Z > 110
	printf("we all go home at 7:10\n");
	printf("we all come tom at 8:15\n");
	#endif
	#ifdef Y
	printf("we all come to class on weekends\n");
	printf("we all come tom at 8:10\n");
	#endif
	}
void funca()
	{
	#undef Z
	#define Z 100
	#if Z == 100
		printf("in funca, val = %d\n", X*X);
		#undef Y
	#endif
	}



