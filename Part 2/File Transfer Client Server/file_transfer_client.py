# Import the necessary libraries

# Import the necessary functions from the socket library
from socket import AF_INET
from socket import error
from socket import socket
from socket import SOCK_STREAM
from time import sleep

# Uninitialised socket at client
s = None

# Standard host is initialised
host = 'localhost'

# Standard port is initialised
port = 8888

# Create the client socket
try:

    # Try to create the client socket with any IP address and TCP Stream
    s = socket(AF_INET, SOCK_STREAM)

# Unable to create client socket
except error as msg:

    # Print appropriate message to the user
    print("Socket creation error:", msg)

# Connect the client socket to the server host and port
try:

    # Try to connect the socket
    s.connect((host, port))

# Unable to connect client socket
except error as msg:

    # Print appropriate message to the user
    print("Socket connection error:", msg)

# Client socket has been created and established, so the transferred file is written
with open('received_file.txt', 'w') as f:

    # Open a new file
    print('file opened')
while True:
    print("To close the server ")

    print(">>>>>>>>")
    ss=input()
    s.send(ss.encode())
    



# Close the file as the writing is complete
f.close()

# Close the socket as data transfer is complete
s.close()
