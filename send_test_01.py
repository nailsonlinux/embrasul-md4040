import socket
import struct

# COMMAND = '010300420064E435' # Measures
# COMMAND = '0111C02C' # Name of device
# COMMAND = '010300440002841E' # UrmsA
COMMAND = '0103000A0001A408' # Ano (Relogio Interno)

IPADDR = '172.16.6.255'
PORTNUM = 1001

#LOG_FILE = "log.txt"

clear_data = list()
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((IPADDR, PORTNUM))
data = COMMAND.decode('hex')
s.send(data)

answer, addr = s.recvfrom(1024)
lol = list(answer)

for item in lol:
	clear_data.append(item)
	
datafile = ''.join(str(e) for e in clear_data)
datafile = datafile.encode('hex_codec')

#file = open(LOG_FILE, "w")
#file.write(datafile)
#file.close()

splited = [datafile[i:i+2] for i in range(0, len(datafile), 2)]

numeric_data = list()
for item in splited:
	numeric_data.append(int(item,16))

# print COMMAND	
print splited
# print numeric_data

s.close()
