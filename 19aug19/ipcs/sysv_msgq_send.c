#include<stdio.h>
#include<sys/ipc.h>
#include<sys/msg.h>
struct msgbuf 
{
	long mtype;
	char mtext[40];
};
void main()
{
	int key=0;	int id=0;	int num=0;
	struct msgbuf vara;
	key = ftok("/bin", 70);
	id = msgget(key, IPC_CREAT|0666);
	printf("enter mtype & msg\n");
	scanf("%d", &num);
	vara.mtype = num;
	scanf("%s", vara.mtext);
	msgsnd(id, &vara, sizeof(vara), 0);
	perror("sending:");
}


