#include<stdio.h>
#include<fcntl.h>
#include<string.h>
#include<sys/mman.h>
#include<unistd.h>
void main()
{
	int fd;
	void *shm;
	fd = shm_open("/name", O_CREAT|O_RDWR, 0666);
	ftruncate(fd, 200);
	shm = mmap(0, 200, PROT_WRITE, MAP_SHARED, fd, 0);
	memset(shm, 0, 200);
	strcpy(shm, "sacred games");
	return;
}
