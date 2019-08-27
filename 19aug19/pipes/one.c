#include<stdio.h>
#include<unistd.h>

void main()
{
	int pd[2], i=0;
	static char buf[20];
	pipe(pd);
	i = fork();
	if(i==0)
	{
		printf("child will write\n");
		write(pd[1], "give me money", 13);
		printf("child has written\n");
	}
	else
	{
		printf("parent will read\n");
		read(pd[0], buf, 3);
		printf("read data is %s\n", buf);
	}
}
