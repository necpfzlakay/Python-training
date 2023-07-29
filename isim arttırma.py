import time

x=input()
y=1

while True:
    while(y!=len(x)):
        z=x[0:y]
        print(z)
        time.sleep(0.1)
        y=y+1

    while y>1:
        z=x[0:y]
        print(z)
        time.sleep(0.1)
        y=y-1

