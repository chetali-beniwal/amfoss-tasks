n=int(input())
l=list(map(int,input().strip().split()))[:n]
lenl=len(l)
for b in range(0,lenl-4):
    c=l[b]+l[b+1]+l[b+2]+l[b+3]
    if c==4:
        l.pop(b)
        l.pop(b+1)
        l.pop(b+2)
        l.pop(b+3)
        l.append(c)
    l.sort()
    lenl=len(l)
for b in range(0,lenl-3):
    c=l[b]+l[b+1]+l[b+2]
    if c<=4:
        l.pop(b)
        l.pop(b+1)
        l.pop(b+2)
        l.append(c)
    l.sort()
    lenl=len(l)
for b in range(0,lenl-2):
    c=l[b]+l[b+1]
    if c<=4:
        l.pop(b)
        l.pop(b+1)
        l.append(c)
    lenl=len(l)
lenl=len(l)
print(lenl)