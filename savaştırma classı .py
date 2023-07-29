import random

class düşman:

    def __init__(self,isim="düşman",kalancan=500,saldırıgücü=10,mermisayısı=5):
        self.isim =isim
        self.kalancan= kalancan
        self.saldırıgücü= saldırıgücü
        self.mermisayısı= mermisayısı

    def saldır(self):
        print(self.isim + "Saldırılıyor...")
        harcananmermi = random.randrange(0,10)
        print(str(harcananmermi)+"kadar mermi karcandı...")
        self.mermisayısı -= harcananmermi
        return(harcananmermi,self.saldırıgücü)

    def saldırıyaugra(self,harcananmermi,saldırıgücü):
        print("Ben Vuruldum...")
        self.kalancan -= (harcananmermi * saldırıgücü)

    def mermibittimi(self):
        if(self.mermisayısı<=0):
            print(self.isim + ": Beyler mermim bitti oyundan çıkıyorum.")
            return True
        return False

    def hayattamı(self):
        if(self.kalancan <=0):
            print("ı AM DIED")

    def printt(self):
        print("İşleniyor...")
        print("İsim:",self.isim,"Kalan can:",self.kalancan,"Saldırı Gücü:",self.saldırıgücü,"Mermi Sayısı:",self.mermisayısı)

düşmanlar =[]

i=0
while(i<10):
    rastgelecan = random.randrange(150,200)
    rastgelesaldırıgücü = random.randrange(10,30)
    rastgelemermi =random.randrange(30,50)
    yenidüşman =düşman("Düşman"+str(i+1),rastgelecan,rastgelesaldırıgücü,rastgelemermi)
    düşmanlar.append(yenidüşman)
    i+=1

i=0
while(i<3):
    randomdüşman1 =random.randrange(0,10)


printt()
hayattamı()