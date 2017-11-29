import struct


def int_128_pack(msg):
    max_int64 = 0xFFFFFFFFFFFFFFFF
    msg = struct.pack(">QQ", (msg >> 64) & max_int64, msg & max_int64)
    return msg


def int_128_unpack(msg):
    a,b = struct.unpack(">QQ", msg)
    unpacked = (a << 64) | b
    return unpacked


def int_32_pack(msg):
    msg = struct.pack("I", msg)
    return msg


def int_32_unpack(msg):
    unpack = struct.unpack("I", msg)
    return unpack[0]
