from pwn import *
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()0123456789_}"
curr = "fitsec{"
end = False
count = 10
while(not(end)):
  for letter in alphabet:
    p = process("ltrace ./ltraceiscool.bin", shell=True)
    p.recvuntil("Enter the flag: ")
    p.sendline(curr + letter)
    print(curr + letter)
    response = p.recvall().decode('utf-8')
    print(response)
    count1 = response.count("\n")
    print(f"{count1}\n")
    if count1 == 26:
      end = True
    if count1 > count:
      curr += letter
      count+=1
      print(f"{curr}")
    p.close()
p.interactive()
