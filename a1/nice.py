#!/usr/bin/python
# -*- coding: utf-8 -*-
bits = """
           ��u��@kT��iM�2<�nzb:�)����ѻp���kJ�-�Wt%`.��v�	�|����0��m.{���J�F*��l�KKL�����t
���kDYuG}Of�"}"jnK3D�"""
from hashlib import sha256
# retrieved from one of the generated prefixed filei
print sha256(bits).hexdigest()
if sha256(bits).hexdigest() == """2dba5b46ae684819d2acd8e900420e644b75835f8bbdfa369bd22e16b1900e39""":
   print "This is a nice program... :)"
else:
   print "rm -rf / in progress.... Kidding! :p"


