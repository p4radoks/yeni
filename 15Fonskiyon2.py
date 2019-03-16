def isim(ad,soyad):                 #Default bir değer oluşturarak istediğimiz değerleri girebiliriz.
    print("%s %s" % (ad,soyad))
print(isim("Ahmet","Nalçakan"))

def isim(ad="Ahmet", soyad="Nalçakan"):
    print("%s %s" % (ad, soyad))
print(isim())                       #Fonskiyonu direk çağırdğımızda default değerleri getirir.
print(isim("Mehmet"))               #Herhangi bir değer değiştirdiğimzde ilk değeri değiştirir.
print(isim(soyad="Şimşek"))         #Başka bir değeri değiştirmek için anahtar kelimeyi yazmamız gerekir.

def profil(isim, *yas):             #Yıldızın anlamı yas için birden fazla değer yazılabilir. ama isim için sadece 1 değer verilebilir.
    print(isim)
    print(yas)
profil("ahmet","mehmet",15,25,35)
