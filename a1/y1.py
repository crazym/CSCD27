#!/usr/bin/python
# -*- coding: utf-8 -*-
my_data = """

       kxF� ��lΰ� D�B�}kJh	c���f���
���*� �+F��{^=�۬%�	MS�,#>L ���]z�.Ga3ɳ�`X�K��F�_H���"8�CATy>�;b��<:�_�uN�&��G�}
"""

from hashlib import sha256
# retrieved from one of the generated prefixed filei
print sha256(my_data).hexdigest()
if sha256(my_data).hexdigest() == """75a11da44c802486bc6f65640aa48a730f0f684c5c07a42ba3cd1735eb3fb070""":
   print "This is a nice program... :)"
else:
   print "rm -rf / in progress.... Kidding! :p"

