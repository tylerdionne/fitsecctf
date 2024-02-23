from pwn import *
p=remote("fitsec-obscure-the-truth.chals.io", 443, ssl=True, sni="fitsec-obscure-the-truth.chals.io")
#p = process("./obscurethetruth.bin")
input = b""
x = "~qlk}{c)l?kG`(jGv(lG`(je"
for char in x:
  input += xor(char, 24)
p.recvuntil(">>>")
p.sendline(input)
print(input)
p.interactive()

