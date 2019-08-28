#include<stdio.h>
#include<sys/stat.h>
#include<mqueue.h>
#include<string.h>

char *buf1 = "monday";
char *buf2 = "tue";
char *buf3 = "wed";
char *buf4 = "thu";

void main()
{
	mqd_t mq;
	struct mq_attr attr;
	mq = mq_open("/usr", O_CREAT|O_RDWR, 0666, NULL);
	perror("mq_open");
	mq_send(mq, buf1, strlen(buf1), 1);
	mq_send(mq, buf2, strlen(buf2), 3);
	mq_send(mq, buf3, strlen(buf3), 2);
	mq_send(mq, buf4, strlen(buf4), 4);
	perror("send");
	mq_close(mq);

}
