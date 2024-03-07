from pwn import *
import ctypes
import time
p = process("./overthetop.bin")
#p = remote("fitsec-over-the-top.chals.io", 443, ssl=True, sni="fitsec-over-the-top.chals.io")
libc = ctypes.CDLL(None)
seed = libc.time(0)
libc.srand(seed)
p.recvuntil(">>>")
p.sendline(b"%d"%1)
ans = 0
for i in range(0, 1001):
  randnum = libc.rand()
  ans += randnum
p.recvuntil(">>>")
p.sendline("%d"%ans)
p.interactive()
