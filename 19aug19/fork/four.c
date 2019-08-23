#include<stdio.h>
#include<unistd.h>
void main()
{
	int i=0;
	int varx=23;
	printf("taki taki rumba pid=%d\n", getpid());
	i=fork();
	printf("ok madam pid=%d i=%d\n", getpid(), i);
	printf("i am rich ppid=%d\n", getppid());
	return;
}
