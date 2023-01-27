# client socket using UDP and IPV4 protocols
# author: Rambod Azimi

# importing socket package
import socket

HOST_NAME = socket.gethostname()
IP_ADDRESS = "127.0.0.1" # local host IP address

# creating a client socket object with the family of INET (IPV4) and of type UDP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:

    # getting an input from the user which is a str representing the domain name
    domain_name_input = input("Please enter the domain name to get the IP address: ")

    # send the encoded version of the domain name to the server using the tuple of IP address and the host name
    client_socket.sendto(domain_name_input.encode(),(IP_ADDRESS, 5050))

    # return type of the recvfrom method is tuple(data, address)
    (data, address) = client_socket.recvfrom(1024)

    # decode the data received from the server
    generated_IP_address = data.decode().strip()

    # print the result to the terminal into str
    print(f"The IP address for the domain name [{domain_name_input}] is [{generated_IP_address}]")

    answer = input("Do you want to try again? (Y/N): ")
    if answer == "Y" or answer == "y":
        continue
    else:
        break
# closing the client socket
client_socket.close()



