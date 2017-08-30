# Import libraries
import socket
import struct
import binascii

# Import local files
import dictionary as dictionary

def convert(array, length):
	if length == 'short':
		data_hex = array[3] + array[4]
		value = int(data_hex, 16)
		return value

	if length == 'float':
		data_hex = array[5] + array[6] + array[3] + array[4]
		x = struct.unpack('>f', binascii.unhexlify(data_hex))
		value = float("{0:.3f}".format(x[0]))
		return value

def talk(command, ip, port):
	clear_data = list()
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect((ip, port))
	data = command.decode('hex')
	s.send(data)
	answer, addr = s.recvfrom(1024)
	received = list(answer)
	for item in received:
		clear_data.append(item)
	datafile = ''.join(str(e) for e in clear_data)
	datafile = datafile.encode('hex_codec')
	splited = [datafile[i:i+2] for i in range(0, len(datafile), 2)]
	numeric_data = list()
	for item in splited:
		numeric_data.append(int(item,16))
	s.close()
	return splited
	
def __debug(command, ip, port):
	entire_command = dictionary.commands[command]
	command_type = entire_command['type']
	command_sequence = entire_command['command']
	raw_data = talk(command_sequence, ip, port)
	return raw_data

def measure(command, ip, port):
	entire_command = dictionary.commands[command]
	length = entire_command['type']
	command_sequence = entire_command['command']
	raw_data = talk(command_sequence, ip, port)
	return convert(raw_data, length)

def measures(ip, port):
	data = {}
	for key, value in dictionary.commands.items():
		data[key] = measure(key, ip, port)
	return data