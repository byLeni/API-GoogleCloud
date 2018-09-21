import socket

# Made by Leni
# Latest Update: Monday. July. 02nd. 2018

HOST = '127.0.0.1'
RECORDER_PORT = 5555

RECODER_ADDR = (HOST, RECORDER_PORT)

FILE_HEADER_SIZE = 44
FILE_READ_SIZE = 8192
BUF_SIZE = 1024

client_recoder = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_recoder.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
client_recoder.connect(RECODER_ADDR)

f = open('__file/2channel_stereo.raw', 'rb')
while True:
    data = f.readline()
    print("data type >> {}".format(data))

    if len(data) == 0:
        client_recoder.send('end'.encode())
        break
    client_recoder.send(data)
print("Sending End")
