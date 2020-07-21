#include<stdio.h>
#include<unistd.h>

void main(){
	int i = 1;
	for (i=0; 1 ; i++){
		printf("running since %d seconds\n", i);
		sleep(1);
	}
	return;
}
