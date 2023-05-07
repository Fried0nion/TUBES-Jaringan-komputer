import socket
import sys

HOST= "0.0.0.0"
PORT= 1234

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Mengikat socket ke alamat dan port tertentu
socket.bind((HOST, PORT))

socket.listen(1)
print('Server is running on:', HOST, '\nPort:', PORT)

while True:
  connectionsocket, addr =  socket.accept()
  print('connected to :', addr)
  msg = connectionsocket.recv(1024).decode()
  print(msg)
  resp= handlerequest()
  connectionsocket.send(resp.encode())
  connectionsocket.close()
socket.close()

def handlerequest():
  responseline = "HTTP/1.1 200 OK \r\n"
  contenttype =  "Content-Type: text/html\r\n\r\n"
  msgbody = "<html><body><h1> Hello Web Server</h1></body></html>"
  response =  responseline + contenttype + msgbody
  return response
