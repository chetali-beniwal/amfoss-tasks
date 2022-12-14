t=int(input())
m=0
l=[]
for a in range(1,t+1):
    n=int(input())
    b=list(map(int,input().strip().split()))[:n]
    b.sort()
    lenb=len(b)
    if lenb<n:
        h=n-lenb
        for c in range(1,h+1):
            b.append(0)
    b.sort()
    e=0
    for e in range(0,lenb-1):
        e1=b[e]
        e2=b[e+1]
        if e1==0:
            g=0
            for e in range(0,lenb-1):
                e0=b[e]
                if e0>0:
                    g+=1
            m=g+1
            break
        elif e1==e2:
            m=lenb
            break
        else:
            m=lenb+1
    l.append(m)
for x in l:
    print(x)