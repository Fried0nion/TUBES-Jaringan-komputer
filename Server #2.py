import socket
import sys

HOST= ""
PORT= 8000

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Mengikat socket ke alamat dan port tertentu
socket.bind((HOST, PORT))

socket.listen(1)
print('Server is running on:', HOST, '\nPort:', PORT)

def handlerequest(request):
    # Split the request into lines
    lines = request.split('\r\n')
    # Extract the requested file name from the first line
    rawsplitfilename = lines[0].split(' ')[1] #masih berbentuk: '/thefilename.html'
    directory, filename = rawsplitfilename.split('/', 1) # directory berisi '/' sedangkan filename sudah berisi nama file 
    

    print("OPENING : ", filename)  # Output: 'thefilename.html'
    try:
        # Open the requested file
        with open(filename, 'r') as file:
            content = file.read()

        # Construct the HTTP response
        response = 'HTTP/1.1 200 OK\r\n'
        response += 'Content-Type: text/html\r\n'
        response += '\r\n'
        response += content
        
    except FileNotFoundError:
        # If the file is not found, construct a 404 response
        response = 'HTTP/1.1 404 Not Found\r\n'
        response += 'Content-Type: text/plain\r\n'
        response += '\r\n'
        response += '404 Not Found'
        
    return response


while True:
  connectionsocket, addr =  socket.accept()
  print('connected to :', addr)
  msg = connectionsocket.recv(1024).decode()
  print(msg)
  resp= handlerequest(msg)
  connectionsocket.send(resp.encode())
  connectionsocket.close()
socket.close()

