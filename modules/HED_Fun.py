import base64
import hashlib

hashing_types = {"md5":hashlib.md5, "sha1":hashlib.sha1, "sha224":hashlib.sha224, "sha384":hashlib.sha384, 
                 "sha256":hashlib.sha256, "sha512":hashlib.sha512, "sha3_224":hashlib.sha3_224, 
                 "sha3_384":hashlib.sha3_384, "sha3_512":hashlib.sha3_512, "shake_128":hashlib.shake_128, 
                 "shake_256":hashlib.shake_256, "blake2b":hashlib.blake2b, "blake2s":hashlib.blake2s}


def Hash(msg, x):
    plain_text = msg.encode("utf-8")
    digest = hashing_types[x](plain_text.strip()).hexdigest()
    return str(digest)


def Encode(msg):
    plain_text = msg.encode("utf-8")
    enc = base64.b64encode(plain_text)
    return str(enc).strip("b''")


def Decode(msg):
    dec = base64.b64decode(msg)
    return str(dec).strip("b''")
