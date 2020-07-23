#include<stdio.h>
#include<fcntl.h>
#include<semaphore.h>
#include<unistd.h>

void main()
{
	sem_t *sem;
	sem = sem_open("/pikachu", O_CREAT|O_RDWR, 0666, 2);
	printf("%d asking for semaphore\n", getpid());
	sem_wait(sem);
	printf("sem acquired\n");
	// critical section
	// write into a shared mem
	// use some resource
	sleep(20);
	printf("will release the semaphore now\n");
	sleep(1);
	sem_post(sem);
	sem_close(sem);
	return;
}
