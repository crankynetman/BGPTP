import ipaddress

foo = open('input/foo.txt', 'rb')                                                                                                                                       
data = foo.read()                                                                                                                                                 
# binary = bin(int.from_bytes(data, byteorder='big'))                                                                                                               
fml = data[0:16]
binary = bin(int.from_bytes(fml, byteorder='big'))
print(binary)
print(len(binary))
ip1 = ipaddress.IPv6Address(fml)
print(ip1)