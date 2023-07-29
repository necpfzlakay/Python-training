import time


x = [int(input()),int(input()),int(input()),int(input())]
q = x[0]
w = x[1]
e = x[2]
r = x[3]

print("Verilen Değerler: " ,x)
a=0
s=0
d=0
f=0
g=0
h=0
j=0

if(q>w):
    a=q
    print(q,w,e,r)
    time.sleep(0.1)
    q=w
    print(q,w,e,r)
    time.sleep(0.1)
    w=a
    print(q,w,e,r)
    time.sleep(0.1)
    
else:
    if(q>e):
        s=q
        print(q,w,e,r)
        time.sleep(0.1)
        q=e
        print(q,w,e,r)
        time.sleep(0.1)
        e=s
        print(q,w,e,r)
        time.sleep(0.1)
    else:
        if(q>r):
            d=q
            print(q,w,e,r)
            time.sleep(0.1)
            q=r
            print(q,w,e,r)
            time.sleep(0.1)
            r=d
            print(q,w,e,r)
            time.sleep(0.1)
        else:
            print(q,w,e,r)
            

if(w>e):
    f=w
    print(q,w,e,r)
    time.sleep(0.1)
    w=e
    print(q,w,e,r)
    time.sleep(0.1) 
    e=f
    print(q,w,e,r)
    time.sleep(0.1)
else:
    if(w>r):
        g=w
        print(q,w,e,r)
        time.sleep(0.1)
        w=e
        print(q,w,e,r)
        time.sleep(0.1)
        e=g
        print(q,w,e,r)
        time.sleep(0.1)
        

if(e>r):
    h=e
    print(q,w,e,r)
    time.sleep(0.1)
    
    e=r
    print(q,w,e,r)
    time.sleep(0.1)
    
    r=h
    print(q,w,e,r)
else:
    print(q,w,e,r)
















    
