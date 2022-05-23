from pwn import *
import string 

flag = "flag{"
print(flag, end = "", file = sys.stderr)
sys.stderr.flush()

pwd = "/home/parallels/Downloads/2022-05-23/small-hashes-anyways"

for i in range(106):
    for c in string.printable:
        testflag = flag + c + " " * (116 - len(flag)-1)
        p = process(["qemu-microblaze", "small_hashes_anyways-bravo39453quebec3/
        small_hashes_anyways"], 
        testflag], 

        env = {"LD_LIBRARY_PATH": pwd+"/microblaze-linux/lib", "QEMU_LD_PREFIX": pwd + "/
        microblaze-linux/"})
        p.sendline(testflag)
        p.readuntil("mismatch")
        k = int(p.readline().split()[0]))
        p.close()
        if k == i + 7:
            flag += c 
            print(c, file = sys.stderr, end = "")
            break 
        # print(7)
        # p.interactive()
        # exit()

print(flag + "}")
