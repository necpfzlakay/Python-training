def geometri (sekil):
    if len(sekil) ==3:
        a =sekil[0]
        b =sekil[1]
        c =sekil[2]
        if ((a + b) > c) and ((a + c) > b) and ((b + c) > a):
            if (a == b) and (a == c) and (c == b):
                print("eşkenar üçgen...")
            elif (a == b) and (a == c):
                print("ikizkenar üçgen...")
            else:
                print("çeşitkenar üçgen...")
        else:
            print("üçgen belirtmemektedir.")

    elif len(sekil)==4:
        a = sekil[0]
        b = sekil[1]
        c = sekil[2]
        d = sekil[3]
        if (a==b) and (a==c) and (a==d):
            print ("kare...")
        elif (a==c) and (b==d):
            print("dikdörtgen...")
        else:
            print("bu herhangi bir basit şekil değildir.")

while (True):
    elemann = int(input("eleman sayınızı giriniz"))
    if(elemann==3):
        a = int(input("kenar a:"))
        b = int(input("kenar b:"))
        c = int(input("kenar c:"))
        geometri([a,b,c])

    elif(elemann==4):
        a = int(input("kenar a:"))
        b = int(input("kenar b:"))
        c = int(input("kenar c:"))
        d = int(input("kenar d:"))
        geometri([a,b,c,d])

    else:
        print("tekrar deneyiniz.")