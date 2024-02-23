from pwn import *
#p=remote("fitsec-math-is-hard.chals.io", 443, ssl=True, sni="fitsec-math-is-hard.chals.io")
p = process("./mathishard.bin")
for i in range(0, 1337):
  p.recvuntil("Number 1 >>>")
  num1 = int(p.recvline())
  p.recvuntil("Number 2 >>>")
  num2 = int(p.recvline())
  p.recvuntil(">>>")
  if i % 4 == 0:
   mynum = num1 - num2
   p.sendline(b"%d"%mynum)
  elif i % 4 == 1:
    mynum = num1 * num2 - i
    p.sendline(b"%d"%mynum)
  elif i % 4 == 2:
    mynum = (num2 + num1) - i
    p.sendline(b"%d"%mynum)
  else:
    mynum = num1 + i * num2
    p.sendline(b"%d"%mynum)
p.interactive()
