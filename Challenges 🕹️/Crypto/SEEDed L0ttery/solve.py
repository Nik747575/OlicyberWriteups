import random,binascii

def xor(key,data):
    res=bytearray()
    for i in range(len(data)):
        res.append(data[i]^key[i%len(key)])
    return res

def decrypt(seed,encrypted_hex):
    random.seed(seed)
    key=random.getrandbits(32).to_bytes(4,"big")
    encrypted_bytes=bytes.fromhex(encrypted_hex)
    return xor(key,encrypted_bytes).decode()

seed=23
ciphertext="8aaf996b9790cb69889cc97fb38dc878b3f69753bef79668dcaea7388af49d5eb382c93dcdbe"
print("FLAG:",decrypt(seed,ciphertext))
