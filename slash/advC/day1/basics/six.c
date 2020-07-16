#include<stdio.h>

void main()
{
	int x = 2, z = 2;
	int y = 3;
	y = ++x * ++x * ++x;
//	     3     4     5
//	     5     5     5
//	   ((++x * ++x) * ++x)
	y = ++z * ++z * ++z * ++z;
//	   (((++x * ++x) * ++x) * ++x)
	++x;
	++x;
	++x;
	y = x*x*x;
	printf("x=%d\n", x);
	printf("y=%d\n", y);
	return;
}
