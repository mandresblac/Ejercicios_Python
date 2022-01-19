import getpass
import sys
import telnetlib
#
HOST = "192.168.56.103"
user123 = "seaccna"
password123 = "seaccna123"
#
#telnet al host x.x.x.x
tn123 = telnetlib.Telnet(HOST) 
#
#Telnet Credentials
tn123.read_until(b"Username:",timeout=1)
tn123.write(user123.encode("ascii") + b"\n")
tn123.read_until(b"Password:",timeout=1)
tn123.write(password123.encode("ascii") + b"\n")
#Config
tn123.write(b"terminal length 0\n")
tn123.write(b"show ip int br\n")
tn123.write(b"exit\n")

#Show output
print(tn123.read_all().decode("ascii"))



#Export output
#readoutput123 = tn123.read_all().decode("ascii")
#saveoutput123 = open("backup_output" + HOST + ".txt", "w")
#saveoutput123.write(str(readoutput123))
#saveoutput123.close()
#print("Archivo Generado")
#
#Force close telnet session
tn123.close()

#