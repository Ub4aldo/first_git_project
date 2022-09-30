print(bytes(4)) #obj 4 bytes long

print(bytes('😄', 'utf-8')) #emoji obj 4 bytes long
mybytes = bytes('😄', 'utf-8')
print(mybytes.decode('utf-8')) #emoji obj 4 bytes long

mybytes = bytearray('😄', 'utf-8') #it creates a bytesarray that can be used as you wish accoriding to the array usage