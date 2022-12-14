#!/bin/python3
import sys
import math

t = int(input().strip())

prime=[2]
counter=0
for a0 in range(t):
    n = int(input().strip())
    prime[counter] = 2
    while(n%2==0):
      prime[counter] = 2
      n=n//2
    for i in range(3,int(math.sqrt(n)+1),2):
      while (n%i==0):
        prime[counter] = i 
        n=n//i

    if(n>2):
      prime[counter]=n  
    counter =counter +1
    prime.append(2) 
prime.pop() 

for p in range(0,len(prime)):
  print(prime[p])
