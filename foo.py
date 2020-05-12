import ipaddress
from bitstring import BitArray

foo = open('input/foo.txt', 'rb')                                                                                                                                       
data = foo.read()
binary = BitArray(data)

 
global_prefix = '01'
file_key = '0000000000001000'

i = 0
index1 = 0
index2 = 110
length = len(binary.bin)

print(data)
print('\n')
print(binary.bin)
print('\n')
print(len(binary.bin))
print('\n')

while index1 < length:
    i += 1
    chunk = binary.bin[index1:index2]
    # print(chunk)
    # print('Iteration: '+ str(i))
    # print('index1')
    # print(index1)
    # print('index2')
    # print(index2)
    # print('\n')

    
    rendered_IP_bin = global_prefix + file_key + chunk
    rendered_IP = ipaddress.IPv6Address(int(rendered_IP_bin, 2))

    print(rendered_IP)
    print('\n')

    index1 += 110
    index2 += 110
