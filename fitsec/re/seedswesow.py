from pwn import *
import ctypes
#p=remote("fitsec-the-seeds-we-sow.chals.io", 443, ssl=True, sni="fitsec-the-seeds-we-sow.chals.io")
p = process("./seedswesow.bin")
libc = ctypes.CDLL(None)
libc.srand.argtypes = [ctypes.c_uint32]
libc.srand(1337)
for i in range(0, 1337):
  randnum = libc.rand()
  libc.srand(randnum)
  p.recvuntil(">>>")
  p.sendline(b"%d"%randnum)
p.interactive()
