
import socket

IP = "127.0.0.1"
PORT = 20000

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.settimeout(1000)
s.connect((IP,PORT))

# send string without carriage return and/or newline
MESSAGE = "HELLO"
s.send(MESSAGE)

# send string without carriage return "\r" and "\n" newline
MESSAGE = "HELLO\r\n"
s.send(MESSAGE)

# send bytes from hex-string
MESSAGE = '0200000000020d0a'.decode('hex')
s.send(MESSAGE)

# close connection
s.close()
