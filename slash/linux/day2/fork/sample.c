#include<stdio.h>
#include<unistd.h>
void main(){
	printf("i am sample my pid=%d, my parent=%d\n", getpid(), getppid());
	sleep(20);
	return;
}
