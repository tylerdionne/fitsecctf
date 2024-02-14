from pwn import *
#p=remote("fitsec-simple-math.chals.io", 443, ssl=True, sni="fitsec-simple-math.chals.io")
p = process("./simplemath.bin")
p.recvuntil("Number 1 >>>")
num1 = int(p.recvline())
p.recvuntil("Number 2 >>>")
num2 = int(p.recvline())
p.recvuntil(">>>")
ans = num1 + num2
p.sendline(b"%d"%ans)
p.interactive()
