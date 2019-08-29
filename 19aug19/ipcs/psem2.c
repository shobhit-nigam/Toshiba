#include<stdio.h>
#include<fcntl.h>
#include<string.h>
#include<sys/mman.h>
#include<unistd.h>
#include<semaphore.h>
void main()
{
	sem_t *sem;
	sem = sem_open("/avatar", O_CREAT|O_RDWR, 0666, 1);
	printf("%d asking for semaphore\n", getpid());
	sem_wait(sem);
	//critical section
	printf("sem acquired\n");
	sleep(6);
	sem_post(sem);
	printf("sem released\n");
	sem_close(sem);
	sem_unlink("/avatar");
	return;
}
