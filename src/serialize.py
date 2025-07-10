import struct
import asyncio

async def packing(fmt,data):
    
    if fmt == str:
        data=data.encode('utf-8')
        pack_data = struct.pack(f'{len(data)}s',data)
        return pack_data
    elif fmt == int:
        pack_data = struct.pack(f'<i',data)
        return pack_data
    elif fmt == float:
        pack_data = struct.pack('<f',data)
        return pack_data
    # elif fmt == "list":
    #     for i in data:
    #         pack = struct.pack(f'<i',i)
    #         print(pack)


async def unpacking(fmt,data):
    
    if fmt == str:
        unpack_data = struct.unpack(f'{len(data)}s',data)[0]
        unpack_data = unpack_data.decode('utf-8')
        return unpack_data
    elif fmt == int:
        unpack_data = struct.unpack(f'<i',data)[0]
        return unpack_data
    elif fmt == float:
        unpack_data = struct.unpack('<f',data)[0]
        return unpack_data

# async def main():
#     while True:
#         data = int(input())
#         pack_data = await packing(int,data)
#         print(pack_data,"pack",type(pack_data))
#         unpack_data = await unpacking(int,pack_data)
#         print(unpack_data,"unpack",type(unpack_data))

# asyncio.run(main())