#!/bin/python3

t=int(input())
for a in range(t):
    n=int(input())
    v=1
    for i in range(2,n+1):
        c=[]
        while v%i!=0:
            for j in range(1,i+1):
                if (v*j)%i==0 and i%j==0:
                    v*=j
                    break
    print(v)
