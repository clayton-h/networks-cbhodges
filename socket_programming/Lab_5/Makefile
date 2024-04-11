# C Makefile
# By: Clayton H.

CC = gcc
CFLAGS = -g -Wall
PROGRAM = c_program
CFILES = socket.c
OBJECTS = socket.o

# Default target
default: $(PROGRAM)

# Rule to link the program
$(PROGRAM): $(OBJECTS)
	$(CC) $(CFLAGS) -o $(PROGRAM) $(OBJECTS)

# Rule to compile object files
%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

# Clean target
clean:
	$(RM) $(PROGRAM) *.o *~

# Run target
run:
	./$(PROGRAM) google.com
