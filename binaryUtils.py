import struct
#lmao thanks wolf for these
def read_uint32(file):
    entry = file.read(4)
    return struct.unpack('<I', entry)[0]

def write_uint32(file, int):
    entry = struct.pack('<I', int)
    file.write(entry)