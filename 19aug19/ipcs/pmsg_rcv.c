#include<stdio.h>
#include<sys/stat.h>
#include<mqueue.h>
#include<stdlib.h>
#include<unistd.h>
void main()
{
	mqd_t mq;
	struct mq_attr *attr;
	char buf[101];
	int prio = 0, i=0;
	attr = malloc(sizeof(struct mq_attr));
	mq = mq_open("/usr", O_CREAT|O_RDWR, 0666, NULL);
	perror("mq_open");
	mq_getattr(mq, attr);
	perror("getattr");
	for(i=0; i<4; i++)
	{
		mq_receive(mq, buf, attr->mq_msgsize, &prio);
		perror("rcv");
		printf("pri=%d\tmsg=%s\n", prio,buf);
		sleep(1);
	}
	mq_close(mq);
	mq_unlink("/usr");
}
