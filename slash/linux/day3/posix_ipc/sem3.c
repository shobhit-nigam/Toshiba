#include<stdio.h>
#include<fcntl.h>
#include<semaphore.h>
#include<unistd.h>

void main()
{
	sem_t *sem;
	sem = sem_open("/pikachu", O_CREAT|O_RDWR, 0666, 1);
	sem_wait(sem);
	// critical section
	// write into a shared mem
	// use some resource
	sem_post(sem);
	sem_close(sem);
	sem_unlink("/pikachu");
	return;
}
