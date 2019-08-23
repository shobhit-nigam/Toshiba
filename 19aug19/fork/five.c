#include<stdio.h>
#include<unistd.h>
void main()
{
	int i=10;
	int varx=23;
	printf("taki taki rumba pid=%d\n", getpid());
	i=fork();
	if(i==0)
	{
		printf("i am child, pid=%d\n", getpid());
	}
	else
	{
		sleep(2);
		printf("i am parent, pid=%d\n", getpid());
	}

//	printf("ok madam pid=%d i=%d\n", getpid(), i);
//	printf("i am rich ppid=%d\n", getppid());
	return;
}
