import random
from numpy import sqrt
import sympy
import math
import time
from tabulate import tabulate

# Extended Euclidean algorithm is implemented below
def extended_gcd(a, b):
    # Initialize the coefficients
    x, y = 0, 1
    last_x, last_y = 1, 0
    while b != 0:
        quotient = a // b
        a, b = b, a % b
        x, last_x = last_x - quotient * x, x
        y, last_y = last_y - quotient * y, y
    return a, last_x, last_y

# modular inverse is calculated below
def modinv(a, m):
   g, x, y = extended_gcd(a, m)
   if g != 1:
       raise ValueError
   return x % m

# double function of the given double and add algorithm for point multiplication
def ecc_double(x1, y1, p, a):
   s = ((3*(x1**2) + a) * modinv(2*y1, p))%p
   x3 = (s**2 - x1 - x1)%p
   y3 = (s*(x1-x3) - y1)%p
   return (x3, y3)

# add function of the given double and add algorithm for point multiplication
def ecc_add(x1, y1, x2, y2, p, a):
   s = 0
   if (x1==x2):
       s = ((3*(x1**2) + a) * modinv(2*y1, p))%p
   else:
       s = ((y2-y1) * modinv(x2-x1, p))%p
   x3 = (s**2 - x1 - x2)%p
   y3 = (s*(x1 - x3) - y1)%p
   return (x3, y3)

# double and add function of the given double and add algorithm for point multiplication
def ecc_double_and_add(pri_key, generator, p, a):
   (resx, resy)=(0, 0)
   (x, y) = generator
   (tmpx, tmpy) = generator
   init = 0
   for i in str(bin(pri_key)[2:]):
       if (i=='1') and (init==0):
          init = 1
       elif (i=='1') and (init==1):
          (resx,resy) = ecc_double(tmpx, tmpy, p, a)
          (resx,resy) = ecc_add(x, y, resx, resy, p, a)
          (tmpx, tmpy) = (resx, resy)
       else:
          (resx, resy) = ecc_double(tmpx, tmpy, p, a)
          (tmpx, tmpy) = (resx, resy)
   return (resx, resy)

def ECC(p,a,b,generator,pri_key):
   return ecc_double_and_add(pri_key, generator, p, a)
def generate_prime(bits):
   return sympy.randprime(2**(bits-1), 2**bits - 1)

def generate_parameters(bit):
   p=generate_prime(bit)
   while(p%4!=3):
      p=generate_prime(bit)
   a = random.randint(1, 100)
   b = random.randint(1, 100)
   while((4*a**3+27*b**2)%p==0):
      a = random.randint(1, 100)
      b = random.randint(1, 100)
   x=random.randint(1,100)
   y=(x**3+a*x+b)%p
   pp=(p+1)//4
   yy=pow(y,pp,p)
   while((yy**2)%p!=y & (p-yy**2)%p!=y):
      x=random.randint(1,p-1)
      y=(x**3+a*x+b)%p
      pp=(p+1)//4
      yy=pow(y,pp,p)
   point=(x,yy)
   return p,a,b,point 

def main():
   table = []
   for i in [128,192,256]:
      time_a=0.0
      time_b=0.0
      time_r=0.0
      for j in range(5):
         p,a,b,generator=generate_parameters(i)
         R=1
         for k in range(3):
            if k==0:
               E=math.sqrt(int(p+1-2*math.sqrt(p))) # lower limit of E
               pri_key=random.randint(2, E-1)
               time_1=time.time()
               time_1=time_1*1000
               pub_key=ECC(p,a,b,generator,pri_key)
               time_2=time.time()
               time_2=time_2*1000
               time_a+=time_2-time_1
               R=R*pri_key
            elif k==1:
               E=math.sqrt(int(p+1-2*math.sqrt(p))) # lower limit of E
               pri_key=random.randint(2, E-1)
               time_1=time.time()
               time_1=time_1*1000
               pub_key=ECC(p,a,b,generator,pri_key)
               time_2=time.time()
               time_2=time_2*1000
               time_b+=time_2-time_1
               R=R*pri_key
            else:
               time_1=time.time()
               time_1=time_1*1000
               shared_key=ECC(p,a,b,generator,R)
               time_2=time.time()
               time_2=time_2*1000
               time_r=time_2-time_1
      time_a=time_a//5
      time_b=time_b//5
      time_r=time_r//5
      table.append([i,time_a,time_b,time_r])
   print(tabulate(table, headers=["K", "A","B","shared key R"], tablefmt="grid"))

#main()