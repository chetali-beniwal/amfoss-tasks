a=int(input())
x=1
l=[]
for x in range(0,a):
    x+=1
    n=int(input())
    b=list(map(int,input().strip().split()))[:n]
    while b[len(b)-1]==0 and len(b)>1:
        b.pop(len(b)-1)
    while b[0]==0 and len(b)>0:
        b.pop()
    lb=len(b)
    e1=b[0]
    c=0
    for e in range (0,lb):
        d=b[e]
        if d%e1!=0:
            l.append("NO")
            c=1
            break
    if lb>=3:
        for e in range(1,lb-1):
            if b[e]==0:
                l.append("NO")
                c=1
                break
    if c!=1:
        l.append("YES")
for k in l:
    print(k)