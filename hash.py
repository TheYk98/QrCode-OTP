import hashlib,binascii
import os,random

def generate_hash(id):                            
    """Hash the id for storage"""
    salt = hashlib.sha256(os.urandom(30)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', id.encode('utf-8'),
                                  salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')



def verify_hash(hashed_id, usr_id):                
    """Verify hashed id against one provided by user"""
    salt = hashed_id[:64]
    hashed_id = hashed_id[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512',
                                  usr_id.encode('utf-8'),
                                  salt.encode('ascii'),
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == hashed_id

