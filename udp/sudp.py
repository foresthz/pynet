import socket, sys

# This code is borrowed from Foundation of Python Network Programming.
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
MAX = 65535
PORT = 1060

s.bind(('0.0.0.0', PORT))
# s.bind(('127.0.0.1', PORT))
print 'listening at', s.getsockname()
while True:
  # 每次最多获取64K的数据?
  data, address = s.recvfrom(MAX)
  print 'the client at', address, 'says', repr(data)
  s.sendto('your data was %d bytes' % len(data), address)

