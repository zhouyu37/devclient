#!/usr/bin/python
# -*- coding:utf-8 -*-
import rsa
import base64
from config import settings

def encrypt(value_bytes):
    key_str = base64.standard_b64decode(settings.PUB_KEY)
    pk = rsa.PublicKey.load_pkcs1(key_str)
    data_list = []
    for i in range(0,len(value_bytes),117):
        chunk = value_bytes[i:i+117]
        result = rsa.encrypt(chunk, pk)
        data_list.append(result)

    return b''.join(data_list)


