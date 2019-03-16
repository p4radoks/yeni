def isim(ad,soyad):                 #Default bir değer oluşturarak istediğimiz değerleri girebiliriz.
    print("%s %s" % (ad,soyad))
print(isim("Ahmet","Nalçakan"))




def isim(ad="Ahmet", soyad="Nalçakan"):
    print("%s %s" % (ad, soyad))
print(isim())                       #Fonskiyonu direk çağırdğımızda default değerleri getirir.
print(isim("Mehmet"))               #Herhangi bir değer değiştirdiğimzde ilk değeri değiştirir.
print(isim(soyad="Şimşek"))         #Başka bir değeri değiştirmek için anahtar kelimeyi yazmamız gerekir.




def profil(isim, *yas):             #Yıldızın anlamı yas için birden fazla değer yazılabilir. ama isim için sadece 1 değer verilebilir. *tuples manasına gelir.
    print(isim)
    print(yas)
profil("ahmet","mehmet",15,25,35)





def profil2(ad,soyad,*yas,**yedikleri):         #2 yıldız o bölümün bir sözlük gibi olduğunu gösterir.
    print(ad,soyad)
    print(yas)
    print(yedikleri)
profil2("ahmet","mehmet",15,25,35,45, elma=2,ceviz=3)   #1. değeri ad'a, 2. değeri soyad'a, ondan sonraki değerleri yas'a ve sözlüğün başladığı yerleri de yediklerine atadı.
profil2("asd","asda",155,6165,65165, karpuz=2)          #Bu şekilde birden fazla profil oluşturabiliriz. Fonksiyonu istediğimiz yerde kullanabiliriz.


def aa(**asd):
    print(asd)




#def mat(a,b,c):
 #   return a+b+c
#sayi=(1,2,8)
#sayi2=(2,3,5,8,5,4)                BU BÖLÜMÜ SOR!
#mat = mat(*sayi)
#mat = mat(*sayi2)
