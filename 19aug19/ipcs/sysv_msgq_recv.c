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
	printf("enter mtype you want to read\n");
	scanf("%d", &num);
	vara.mtype = num;
	msgrcv(id, &vara, sizeof(vara), vara.mtype ,0);
	perror("rcv:");
	printf(",sg rcvd --> %s\n", vara.mtext);
}


