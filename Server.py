# server socket using UDP and IPV4 protocols
# author: Rambod Azimi

# importing socket package
import socket

dns_table = {
    "www.twitter.com" : "104.244.42.193",
    "www.amazon.com" : "65.8.193.142",
    "www.amazon.ca" : "13.35.79.127",
    "www.google.ca" : "142.250.81.227",
    "www.mcgill.ca" : "132.216.177.160",
    "www.rambodazimi.com" : "162.55.240.80",
    "www.gmail.com" : "142.251.40.133",
    "www.instagram.com" : "31.13.71.174"
}

# creating a server socket object with the family of INET (IPV4) and of type UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Server is starting...")

# binding the server socket to the local host with the port 5050
server_socket.bind(("127.0.0.1", 5050))

while True:

    (data, address) = server_socket.recvfrom(1024)

    # decode the data to str
    decoded_data = data.decode()

    generated_IP_address = dns_table.get(decoded_data, "Sorry! The website is not in the dns database of the server!").encode()
    send_to_client = server_socket.sendto(generated_IP_address, address)