import ipaddress
from bitstring import BitArray
from pprint import pprint

foo = open('input/foo.txt', 'rb')                                                                                                                                       
data = foo.read()
binary = BitArray(data)

padding_value = '0'
chunk_size = 110
global_prefix = '01'
file_key = '0000000000001000'

counter = 0
index1 = 0
index2 = chunk_size
length = len(binary.bin)

dict = {
    "Prefix": "",
    "TLV_1": [],
    "TLV_2": "",
    "TLV_3": "",
}

while index1 < length:
    #print(counter)

    chunk = binary.bin[index1:index2]
    chunk_length = len(chunk)

    if chunk_length < 110:
        padding_size = chunk_size - chunk_length
        padding_value = padding_value * padding_size

        chunk = str(padding_value) + chunk
        padding_tlv = "0011" + format(padding_size, '028b')
        dict["TLV_3"] = padding_tlv
    
    IP_bin = global_prefix + file_key + chunk
    rendered_IP = ipaddress.IPv6Address(int(IP_bin, 2))

    prefix = str(rendered_IP) + "/128"

    chunk_tlv = "0010" + format(counter, '028b')

    dict["Prefix"] = prefix
    # dict["TLV_1"]
    dict["TLV_2"] = chunk_tlv
    


    index1 += 110
    index2 += 110
    counter += 1

    pprint(dict)
