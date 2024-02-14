from pwn import *
#p=remote("fitsec-clairvoyance.chals.io", 443, ssl=True, sni="fitsec-clairvoyance.chals.io")
p = process("./clairvoyance.bin")
p.recvuntil(">>>")
p.sendline()
p.interactive()

