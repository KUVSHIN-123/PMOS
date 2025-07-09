import struct


def packing(fmt,data):
    
    if fmt == "str":
        data=data.encode('utf-8')
        pack_data = struct.pack(f'{len(data)}s',data)
        return pack_data
    elif fmt == 'int':
        pack_data = struct.pack(f'<i',data)
        return pack_data
    elif fmt == 'float':
        pack_data = struct.pack('<f',data)
        return pack_data

data = int(input())
print(packing('int',data))