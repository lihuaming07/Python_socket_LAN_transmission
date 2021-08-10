import socket


hostName = socket.gethostname()
host = socket.gethostbyname(hostName)

print(hostName)
print(host)
