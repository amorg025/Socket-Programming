#import socket module
from socket import *
import sys 

# Create a server socket
serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepare a server socket
serverPort = 6789  #
serverSocket.bind(('', serverPort))
serverSocket.listen(1)  

print(f"The server is ready to receive connections on port {serverPort}")

while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()

    try:
        # Receive the HTTP request message
        message = connectionSocket.recv(1024).decode()  
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        
        # Send HTTP headers into the socket
        response_headers = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"
        connectionSocket.send(response_headers.encode())

        # Send the content of the requested file to the client
        connectionSocket.send(outputdata.encode())

        connectionSocket.close()
    except IOError:
        # Send a 404 Not Found response message
        not_found_response = "HTTP/1.1 404 Not Found\r\n\r\n<h1>404 Not Found</h1>"
        connectionSocket.send(not_found_response.encode())
        connectionSocket.close()

# Close the server socket
serverSocket.close()
sys.exit() 
