class düşman:
    kkalancan  = 3
    def saldır(self):
        print ("Aslanım saldır annnesine hükmet onun. KUŞUM BEN AMK NASIL SALDIRAYIM CİK CİK.")
        self.kkalancan -=1
    def hayattamı(self):
        if (self.kkalancan<=0):
            print("enemy has been slain")
        else:
            print(str(self.kkalancan) + "canım kaldı...")


düşman2=düşman()

düşman2.saldır()
düşman2.saldır()
düşman2.saldır()
düşman2.hayattamı()

"""elif (kalancan == 2):
print("Haydi kartallll.")
self.kalancan -= 1
elif (kalancan == 1):
print("KUŞUM BEN AMK NASIL SALDIRAYIM CİK CİK.")
self.kalancan -= 1
else:
print("kalan canım: " + self.kalancan)"""



