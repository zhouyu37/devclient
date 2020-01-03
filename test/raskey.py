# -*- coding: utf-8 -*-
import rsa
import base64
(pubkey, privkey) = rsa.newkeys(1024)

# pub = pubkey.save_pkcs1()
# print(pub)
#
# pri = privkey.save_pkcs1()
# print(pri)
pubkey = base64.encodestring(pubkey.save_pkcs1())
privkey = base64.encodestring(privkey.save_pkcs1())
print(pubkey)
print(privkey)