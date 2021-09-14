import socket

print("este script verifica se um dominio existe ou nao ")
nome = input()
#hostName = "infosi.gov.ao"
try:
    ipAddress = socket.gethostbyname(nome)
    print("o dominio esta disponivel")
except socket.gaierror:
    print("*******************")
    print("\nDominio nao xiste")
#print("IP address of the host name {} is: {}".format(hostName, ipAddress))
