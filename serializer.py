import base64

BASE62 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

# Base62 encoding

def encode_base62(n: int) -> str:
    if n == 0:
        return "0"
    s = []
    while n > 0:
        s.append(BASE62[n % 62])
        n //= 62
    return "".join(reversed(s))

def decode_base62(s: str) -> int:
    n = 0
    for ch in s:
        n = n * 62 + BASE62.index(ch)
    return n


# Bitmap encoding

def serialize_bitmap(nums: set[int]) -> str:
    bits = [0] * 300
    for n in nums:
        bits[n - 1] = 1

    b = bytearray()
    for i in range(0, 300, 8):
        byte = 0
        for j in range(8):
            if i + j < 300:
                byte = (byte << 1) | bits[i + j]
        b.append(byte)

    return "B" + base64.b64encode(bytes(b)).decode("ascii")


def deserialize_bitmap(s: str) -> set[int]:
    raw = base64.b64decode(s[1:])
    bits = []
    for byte in raw:
        for i in range(7, -1, -1):
            bits.append((byte >> i) & 1)
    return {i + 1 for i, b in enumerate(bits[:300]) if b == 1}


# Small-set encoding

def serialize_small(nums: set[int]) -> str:
    return "S" + ",".join(encode_base62(n) for n in sorted(nums))


def deserialize_small(s: str) -> set[int]:
    parts = s[1:].split(",")
    return {decode_base62(p) for p in parts}


# Hybrid serialize/deserialize

def serialize(nums: set[int]) -> str:
    if len(nums) < 30:
        return serialize_small(nums)
    return serialize_bitmap(nums)


def deserialize(s: str) -> set[int]:
    if s.startswith("B"):
        return deserialize_bitmap(s)
    if s.startswith("S"):
        return deserialize_small(s)
    raise ValueError("Unknown format")
