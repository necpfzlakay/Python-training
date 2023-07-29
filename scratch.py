print("     Merhaba sayın kullanıcılar 'OKULUN EN GÜZEL KIZLARI' adlı oyunumuza hoş geldiniz,\n     Keşke gelmeseydiniz çünki bunu oynayan Khaslı kızlar intihara sürükleniyor:)")

print("                 Neyse fazla uzatmadan oyunumuza başlayalım bakalım")
print(".")

print("         Oyunumuz şöyle:  Kadir Has Üniversitesi içerisinde size göre en güzel 5 kızın isimlerini ve soy isimlerini")
print("         yazıp puanlandırmanız gerekmektedir. Onünüze çıkan açıklamalar sizi yönlendirecektir...")
print(".")
print("                 Hazırsanız başlayalım :)))")
print(".")
print("     Öncelikle")

a = input("     İlk Kızın Bilgilerini Yazınız:   ")

b = input("     ikinci Kızın Bilgilerini Yazınız:    ")

c = input("     üçüncü Kızın Bilgilerini Yazınız:    ")

d = input("     dördüncü Kızın Bilgilerini Yazınız:  ")

e = input("     beşinci Kızın Bilgilerini Yazınız:   ")

print(".")
print("     Veriler işleniyor...")
print(".")
print("     database yenileniyor...")
print(".")
print("     kızlar loading...")
print(".")
kizlar = [a, b, c, d, e]

print("   1.Kız:  {} \n   2.Kız:  {} \n   3.Kız:  {} \n   4.Kız:  {}\n   5.Kız:  {}".format(kizlar[0], kizlar[1], kizlar[2], kizlar[3], kizlar[4]))
print(".")
print(".")
print("    Evvet şimdi yapman gereken ise her kız için sırasıyla 0/10 arasında puanlandırmak:")
print(".")
print(".")
p0 = int(input("      '  {}  '     hakkında düşündüğün puanı yaz:    ".format(kizlar[0])))
p1 = int(input("      '  {}  '     hakkında düşündüğün puanı yaz:    ".format(kizlar[1])))
p2 = int(input("      '  {}  '     hakkında düşündüğün puanı yaz:    ".format(kizlar[2])))
p3 = int(input("      '  {}  '     hakkında düşündüğün puanı yaz:    ".format(kizlar[3])))
p4 = int(input("      '  {}  '     hakkında düşündüğün puanı yaz:    ".format(kizlar[4])))



