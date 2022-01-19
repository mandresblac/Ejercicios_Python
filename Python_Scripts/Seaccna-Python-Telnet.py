import telnetlib
HOST = "192.168.56.104"
user123 = "seaccna"
password123 = "seaccna123"
#TELNET AL HOST x.x.x.x
tn123 = telnetlib.Telnet(HOST)
#TELNET CREDENTIALS
tn123.read_until(b"Username:",timeout=1)
tn123.write(user123.encode("ascii") + b"\n")
tn123.read_until(b"Password:",timeout=1)
tn123.write(password123.encode("ascii") + b"\n")
#Configuration Commands
tn123.write(b"terminal length 0\n")
tn123.write(b"show ip int br\n")
tn123.write(b"show run all\n")
tn123.write(b"exit\n")
#Export output
readoutput123 = tn123.read_all().decode("ascii")
saveoutput123 = open("SeaCCNA_Youtube" + HOST + ".txt", "w")
saveoutput123.write(str(readoutput123))
saveoutput123.close()
print("Archivo Generado")
#Show output
#print(tn123.read_all().decode("ascii"))
#Force close telnet session
tn123.close()

