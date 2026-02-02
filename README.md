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
...
