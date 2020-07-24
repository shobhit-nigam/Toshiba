output:	app.o one.o two.o three.o
	gcc app.o one.o two.o three.o -o output

app.o:	app.c app.h 
	gcc -c app.c

one.o:	one.c a.h app.h
	gcc -c one.c

two.o:	two.c b.h
	gcc -c two.c

three.o: three.c c.h
	gcc -c	three.c

clean:
	rm -f *.o
