import getpass
import sys
import telnetlib

tn =telnetlib.Telnet("192.168.56.103", "23")
user = input("Enter your username: ")
password = getpass.getpass()
print("About to call tn.read")
tn.read_until(b"Username: ")
print("About to write username")
tn.write(user.encode("ASCII") + b"\n")
if password:
    print("Looking for password prompt")
    tn.read_until(b"Password: ")
    print("About to write password")
    tn.write (password.encode("ASCII") + b"\n")
tn.write(b"terminal length 0\n")
tn.write(b"show ip int br\n")
print(tn.read_all())
tn.close()