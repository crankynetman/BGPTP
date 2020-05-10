foo = open('foo.txt', 'rb')                                                                                                                                       
data = foo.read()                                                                                                                                                 
binary = bin(int.from_bytes(data, byteorder='big'))                                                                                                               
print(binary)

blob = int(binary, base=2)
blobbytes = blob.to_bytes(1000,byteorder='big')

with open('test.txt', 'wb') as file:
    file.write(blobbytes)

