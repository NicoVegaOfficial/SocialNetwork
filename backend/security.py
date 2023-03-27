import hashlib
from random import randrange

def securepwd(x):
    r = hashlib.sha512(x.encode())
    return r.hexdigest()


def random_salt():
    secure_string = ""
    secure_list = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","g","h","j","k","l","z","x","c","v","b","n","m","1","2","3","4","5","6","7","8","9", "0"]
    for x in range(16):
        secure_random = randrange(len(secure_list))
        secure_string = secure_string + secure_list[secure_random]
    return secure_string
