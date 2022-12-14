#!/bin/python3

import sys

sum=[0]
counter=0

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    for i in range(1,n):
      if i%3==0 or i%5==0 :
        sum[counter] = sum[counter] + i
    counter=counter+1
    sum.append(0)

sum.pop()

for s in range(0,len(sum)):
  print(sum[s])