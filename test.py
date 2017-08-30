import struct, binascii
hexbytes = "435AA36A"

x = struct.unpack('>f', binascii.unhexlify(hexbytes))
print("RESULT:" + str(x))