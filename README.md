# Lab 2

## Team Members
Kamron Rousseau
Adit Bansal

## Lab Question Answers

Lab Manual Q1: Some of the messages sent did not appear. This is because UDP is unreliable with no packet recovery mechanism.

Lab Manual Q2: All numbers still sent in the server, just slower. TCP is reliable with packet loss handling.

Code Q1: Argc is an integer that tells you how many arguments were passed in the command line. Argv is an array of strings where each string is an argument in the command line. It contains the port number as a string.

Code Q2: A UNIX file descriptor is an integer used to identify and keep track of open files or I/O resources. A file descriptor table takes those file descriptor numbers and maps them to the actual open file objects in the kernel. This allows the kernel to know what each integer refers to.

Code Q3: A struct is a user-defined data type that allows you to store data of different types under one variable. Sockaddr_in is a struct that stores socket address information such as IP address, port number, and address family.

Code Q4: The input parameters of socket() are domain which specifies the address family, type which specifies the type of communication behavior, and protocol which specifies the type of communication protocol to use (TCP or UDP).

Code Q5: bind() takes in the socket file descriptor that was created by socket to identify which socket is being bound, a struct containing the local IP address and port number, and the size of the address struct in bytes.
listen() takes in the bound file descriptor and the maximum number of allowed pending connections.

Code Q6: While(1) creates an infinite loop that allows the server to continuously accept new connections. If there were multiple connections to handle, since the code handles clients one at a time, other clients would experience delays or refusal of service.

Code Q7: fork() works by creating a new process called a child process that is almost identical to the parent. This allows for a server to handle multiple clients at a time. It could be implemented here by accepting a connection, forking a child process, and letting the child handle the client while the parent can accept a new connection.

Code Q8: A system call is a safe and controlled way for a user-level program to request operating system-level services such as file I/O or network communication. It allows programs to safely access files, use network sockets, allocate memory, create processes, or communicate with hardware, all while preventing programs from crashing or corrupting the system.
