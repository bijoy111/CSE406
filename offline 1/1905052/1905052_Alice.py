import importlib
import math
import socket
from numpy import sqrt 
import random 

elliptic_curve_module=importlib.import_module("1905052_ellipticCurve")
ECC=elliptic_curve_module.ECC
aes=importlib.import_module("1905052_AES")
allRoundkeys=aes.allRoundkeys
divide_into_substrings=aes.divide_into_substrings
xor_strings=aes.xor_strings
aesEncryption=aes.aesEncryption
   
s = socket.socket() # a socket object is created        
port = 12345 # a port number is created to connect with server
s.connect(('127.0.0.1', port)) # Alice is connected to the server

p=17
E=int(p+1-2*math.sqrt(p)) # lower limit of E
a=2
b=2
generator=(5,1)

pri_key=random.randint(2, E-1)
pub_key=ECC(p,a,b,generator,pri_key)
print("Public Key: ",end="")
print(pub_key)

tmp=pub_key
v1,v2=map(str,tmp)
s.send(v1.encode())
s.send(v2.encode())

response = s.recv(1024).decode()
x=int(response)
response = s.recv(1024).decode()
y=int(response)
point=(x,y)
#print(point)

shared_key=ECC(p,a,b,point,pri_key)

print("Shared Key: ",end="")
print(shared_key)

kkey=shared_key[0]
kkey=str(kkey)
kkey=kkey.ljust(16)
keys=allRoundkeys(kkey)
#print(kkey)
Plaintext="This is the first offline of cse 406 sessional course."
Plaintext=str(Plaintext)
Plaintexts=divide_into_substrings(Plaintext)
#IV = "0" * 16
IV=str(shared_key[1])
IV=IV.ljust(16)
cipherText=""
for Plaintext in Plaintexts:
    Plaintext=Plaintext.ljust(16)      
    Plaintext=xor_strings(Plaintext,IV)      
    ciph=aesEncryption(Plaintext,keys)
    cipherText+=ciph
    IV=ciph
print(cipherText)


cipherText=str(cipherText)
s.send(cipherText.encode())
while True:
    pass

# close the connection 
s.close()