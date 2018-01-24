import socket
def num(s):
    try:
        return int(s)
    except ValueError:
        return -1
TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print 'Connection address:', addr
while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    data = num(data)
    Result = 1
    if data == -1:
        conn.send("Fail Number")
    elif data<0:
        conn.send("Number Not Negative Number")
    else:
        for x in range(1, data+1):
            Result *=x
        conn.send(str(Result))  # echo
        print "Received Result:", Result
    conn.close()
