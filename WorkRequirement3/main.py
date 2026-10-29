"""Import socket module from the library"""
import socket

def resolve_hostname():
    """Function to resolve a hostname from user input"""
    hostname = input("Enter a hostname: ")

    #Gets the IP address by using the socket module library and gethostbyname function
    get_address = socket.gethostbyname(hostname)

    #Prints the hostname typed by the user input and its resolved IP address
    print(f"Hello from: {hostname}! The IP address is {get_address}" )

resolve_hostname()
