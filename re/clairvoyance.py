from pwn import *
import ctypes
#p=remote("fitsec-clairvoyance.chals.io", 443, ssl=True, sni="fitsec-clairvoyance.chals.io")
p = process("./clairvoyance.bin")
libc = ctypes.CDLL(None)
libc.srand.argtypes = [ctypes.c_uint32]
libc.srand(2024)
randnum = libc.rand()
p.recvuntil(">>>")
p.sendline(b"%d"%randnum)
p.interactive()

