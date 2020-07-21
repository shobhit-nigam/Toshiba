#include<stdio.h>
#include<unistd.h>
#include<fcntl.h>

void main(){
	int pid=0, fd=0;
	static char buf[20];
	//create()
	fd = open("newquotes.txt", O_WRONLY|O_CREAT, 0666); 
	printf("fd for new_quotes.txt is %d\n", fd);
	read(0, buf, 14);
	printf("read data = %s\n", buf);
	write(fd, buf, 10);
	close(fd);
	return;
}
