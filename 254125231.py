import time
import random

can = int(random.randrange(1,100))

print(can)

time.sleep(3)

i = can
while True:  
    if(can > 0):
        print("hayattasın...")
        can-=1
        print("             ", can)
        time.sleep(0.1)
    else:
        print("öldün...")
        break
#dsfgsdgdds
