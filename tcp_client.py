"""
Server receiver buffer is char[256]
If correct, the server will send a message back to you saying "I got your message"
Write your socket client code here in python
Establish a socket connection -> send a short message -> get a message back -> ternimate
use python "input->" function, enter a line of a few letters, such as "abcd"
"""
import socket

def main():
    # TODO: Create a socket and connect it to the server at the designated IP and port
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # TODO: Get user input and send it to the server using your TCP socket
    server_address = ('172.20.10.2', 12345) 
    client_socket.connect(server_address)
    # TODO: Receive a response from the server and close the TCP connection
    try:
        message = input("Enter a message to send: ")    #getting user input
        
        client_socket.sendall(message.encode())             #sending data
        
        data = client_socket.recv(256)                        #receive data
        print(f"Received from server: {data.decode()}")
        
    finally:
        
        client_socket.close()                   #close the connection
    pass


if __name__ == '__main__':
    main()
