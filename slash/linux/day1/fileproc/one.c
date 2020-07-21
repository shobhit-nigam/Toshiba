#include<stdio.h>
#include<unistd.h>

void main(){
	int pid;
	pid = getpid();
	printf("my pid = %d\n", pid);
	return;
}
