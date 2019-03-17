def isim(ad,soyad):                 #Default bir değer oluşturarak istediğimiz değerleri girebiliriz.
    print("%s %s" % (ad,soyad))     #FONKSİYONU BU ŞEKİLDE KULLANDIĞIMIZ TAKTİRDE ÖNCE BOŞ DEĞER DÖNDÜRÜR. DAHA SONRA PRİNTLERE GEÇER VE ONLARI TEKER TEKER FONKSİYON İÇİNDE YERLEŞTİREREK DÖNDÜRÜR.
print(isim("Ahmet","Nalçakan"))
print(isim("Mehmet","Güven"))

"""

def isim(ad,soyad):                 #Yukarıda yazdığım fonksiyonun kullanılması gereken hali budur. Print içerisinde yazdığım isimleri return içerisinde döndürerek yazdırır.
    return(%s %s %(ad,soyad)
print (isim("Mehmet","Nalçakan"))       DÜZELTME!!!
print(isim("Mehmet","Güven"))

def isim(ad,soyad):                 #Yukarıda yazdığım fonksiyonun kullanılması gereken diğer şekli de budur. Farkı ise dışarıda fonksiyonun değerlerini belirleyip fonksiyon içerisine gönderir ve ekrana yazdırır.
    print(%s %s %(ad,soyad))
isim("Mehmet","Nalçakan")
isim("Mehmet","Güven")

"""



def isim(ad="Ahmet", soyad="Nalçakan"):
    return "%s %s" % (ad, soyad)
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


def aa(**asd):          #Dışardan bir sözlüğü fonksiyona atama
    print(asd)
a={"a":1,"b":2}
b={"a":2,"b":3}
aa(**a)
aa(**b)

def mat(a,b,c):         #Dışardan bir Tuples'ı fonksiyona atama
    print(a+b+c)
dizi1=(1,2,3)
mat(*dizi1)
dizi2=(2,3,4)
mat(*dizi2)





