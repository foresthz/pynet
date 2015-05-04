
import socket, sys
import config as cfg
PORT = 1060
MAX=65535

print '--- length of arguments', len(sys.argv)
if len(sys.argv)>1:
  msg = '_'.join(sys.argv[1:])
else:
  msg = "default message"
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print 'address before sending' #, s.getsockname()
s.sendto(msg, (cfg.options['server'], PORT))
print  'address after sending', s.getsockname()
data, address = s.recvfrom(MAX)
print 'the server', address, 'says', repr(data)


