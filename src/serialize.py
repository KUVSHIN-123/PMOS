import msgpack

# Сериализация
def serialize(data):
    return msgpack.packb(data, use_bin_type=True)

# Десериализация
def deserialize(binary_data):
    return msgpack.unpackb(binary_data, raw=False)