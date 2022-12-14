#!/bin/python3
import sys


t = int(input().strip())
even_sum = [2]
s=0
for a0 in range(t):
    n = int(input().strip())
    fib_seq=[1,2]
    fib_even=[2]
    i=2
    while fib_seq[-1] < n:
      temp = fib_seq[i-1]+fib_seq[i-2]
      if (temp<n):
        fib_seq.append(temp) 
        if((fib_seq[i])%2==0):
          fib_even.append(fib_seq[i])
          even_sum[s]=even_sum[s]+fib_seq[i]
      else: 
        break
      i=i+1
    s=s+1
    even_sum.append(2)

even_sum.pop()
print(even_sum)