faktöriyel =1

while True:
    sayı= int(input("sayı giriniz.:"))
    if (sayı<=0):
        print("girdiğiniz sayı 0'dan küçük olamaz.")
    else:
        for sa in range(1,sayı+1):

            faktöriyel *= sa
        print("faktöriyeli:", faktöriyel)












