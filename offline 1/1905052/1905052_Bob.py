import importlib
import math
import socket   
from numpy import sqrt 
import random  

elliptic_curve_module=importlib.import_module("1905052_ellipticCurve")
ECC=elliptic_curve_module.ECC
aes=importlib.import_module("1905052_AES")
allRoundkeys=aes.allRoundkeys
divide_into_subHex=aes.divide_into_subHex
xor_strings=aes.xor_strings
aesDecryption=aes.aesDecryption
  
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

response = s.recv(1024).decode()
x=int(response)
response = s.recv(1024).decode()
y=int(response)
point=(x,y)

shared_key=ECC(p,a,b,point,pri_key)

print("Shared Key: ",end="")
print(shared_key)

tmp=pub_key
v1,v2=map(str,tmp)
s.send(v1.encode())
s.send(v2.encode())

kkey=shared_key[0]
kkey=str(kkey)
kkey=kkey.ljust(16)
keys=allRoundkeys(kkey)
#print(kkey)

cipherText=s.recv(1024).decode()
cipherText=str(cipherText)
#print(cipherText)


plaintext=''
#IV = "0" * 16 
IV=str(shared_key[1])
IV=IV.ljust(16)
cipherTexts=divide_into_subHex(cipherText)
for cipherText in cipherTexts:
    ciph=aesDecryption(cipherText,keys)
    ciph=xor_strings(ciph,IV)
    IV=cipherText
    plaintext+=ciph
print(plaintext)

while True:
    pass

# close the connection 
s.close()