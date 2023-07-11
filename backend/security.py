import hashlib
import secrets

def securepwd(x):
    r = hashlib.sha512(x.encode())
    return r.hexdigest()


def random_salt():
    return secrets.token_hex(16)