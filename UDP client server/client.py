import socket

servername = "127.0.0.6"
serverport = 12000

clientsocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

message = input("INPUT SENTENCE TO UPPER : ")
clientsocket.sendto(message.encode(),(servername,serverport))
modifiedmsg , serveraddress = clientsocket.recvfrom(2048);
print(f"server add is {serveraddress}")
print(modifiedmsg.decode())

clientsocket.close();
