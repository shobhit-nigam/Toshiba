#include<stdio.h>
#include<sys/stat.h>
#include<mqueue.h>

void main()
{
	mqd_t mq;
	struct mq_attr attr;
	mq = mq_open("/usr", O_CREAT|O_RDWR, 0666, NULL);
	perror("mq_open");
	mq_send(mq, "hello", 6, 1);
	perror("send");
	mq_close(mq);

}
