import struct
import asyncio

async def packing(data):
    data_type = await set_type(data)
    match data_type:
        case "str":
            data=data.encode('utf-8')
            data_type=data_type.encode('utf-8')
            pack_data = struct.pack(f'{len(data)}s',data)
            return data_type,pack_data
        case "int":
            pack_data = struct.pack(f'<i',data)
            data_type=data_type.encode('utf-8')
            return data_type,pack_data
        case "float":
            pack_data = struct.pack('<f',data)
            data_type=data_type.encode('utf-8')
            return data_type,pack_data

async def unpacking(data_type,data):
    data_type = data_type.decode('utf-8')
    match data_type:
        case "str":
            unpack_data = struct.unpack(f'{len(data)}s',data)[0]
            unpack_data = unpack_data.decode('utf-8')
            return unpack_data
        case "int":
            unpack_data = struct.unpack(f'<i',data)[0]
            return unpack_data
        case "float":
            unpack_data = struct.unpack('<f',data)[0]
            return unpack_data

async def set_type(data):
    match data:
        case str():
            return "str"
        case int():
            return "int"
        case float():
            return "float"

# async def main():
#     while True:
#          data = input()
#          data_type,pack_data = await packing(data,data)
#          print(pack_data,"pack",type(pack_data))
#          unpack_data = await unpacking(data_type,pack_data)
#          print(unpack_data,"unpack",type(unpack_data))
    
# asyncio.run(main())