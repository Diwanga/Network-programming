import socket

servername = "127.0.0.6"
serverport = 12000

serversocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serversocket.bind((servername,serverport))

print("server is ready to communicate....")

while True :
    message ,clientaddress= serversocket.recvfrom(2048)
    print(clientaddress)
    modifiedmsg = message.decode().upper()
    serversocket.sendto(modifiedmsg.encode(),clientaddress)
