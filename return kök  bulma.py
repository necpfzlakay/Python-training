def karekök(a,b,c):

    delta = (b*b - 4*a*c)
    if (delta<0):
        print("DENKLEMİN REEL'GERÇEK'KÖKÜ YOKTUR.")
        return
    elif(delta==0):
        x1 = (-b - delta ** 0.5) // (2 * a)
        x2 = (-b + delta ** 0.5) // (2 * a)
        print("çift katlı kök vardır:")
        return(x1,x2)
    else:
        x1 = (-b - delta ** 0.5)/(2*a)
        x2 = (-b + delta ** 0.5)/(2*a)
        return (x1,x2)


while True:
    a = int(input("A:"))

    b = int(input("B:"))

    c = int(input("C:"))

    sonuc = karekök(a,b,c)

    print(sonuc)

