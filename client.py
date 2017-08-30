import md4040 as md4040
import devices as d

alldata = {}

for key, value in d.devices.items():
	alldata[key] = md4040.measures(value['ip'], value['port'])

def display():
	for key, value in alldata.items():
		print key
		print "---"
	for nkey, nvalue in value.items():
		print nkey + ": " + str(nvalue)

display()