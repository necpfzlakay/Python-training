

AD = "12345"
şifre = "necip"

while(True):
    kullanıcıadı = input("kulanıcı adınızı giriniz:  ")
    şifresi= input("şifrenizi giriniz:   ")
    if ((AD==kullanıcıadı) and (şifre==şifresi)):
        print ("giriş başarı ile gerçekleştirildi",AD)
        break
    elif ((AD!=kullanıcıadı) and (şifre==şifresi)):
        print ("kullanıcı adınızı yanlış girdiniz. \n      lütfen tekrar deneyiniz...")
    elif((AD!=kullanıcıadı) and (şifre!=şifresi)):
        print("kullanıcı adı ve şifrenizi yanlış girdiniz... Tekrar deneyiniz")
    elif ((AD==kullanıcıadı) and (şifre!=şifresi)):
        print("yanlış şifre girildi.\n şifrenizi mi unuttunuz?  şifrenizi yenilemek için 'yenile' yazınız")
        cevap = input()
        if (cevap == "yenile"):
            yenişifre = input("Yeni şifrenizi giriniz: ")
            if (yenişifre!=şifre):
                print ("veri tabanı düzenleniyor")
                şifre=yenişifre
                print(".")
                print("Şifreniz başarıyla değiştirildi... Lütfen tekrar giriş yapınız.")
            elif (yenişifre == şifre):
                print("YENİ ŞİFRENİZ ESKİ ŞİFRENİZLE AYNI OLAMAZ!")
    else:
        print ("tekrar deneyiniz")