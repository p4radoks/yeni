import math
class insan:                                #Sınıfımızı oluşturduk
    gozrengi="kahverengi"                   #Bu bölüm sınıfımızın özellikleri
    parmaksayisi=15
    def metot (self):                       #Sınıfımıza ait fonksiyon NOT: self fonksiyona dışardan erişilenbilmesini sağlar
        return "Bu metot çalıştı!"          #Bu metot sadece sınıfa ait. Sınıf içerisindeki değerleri döndürür.

yeniinsan=insan()                           #Yeniinsan insan sınıfından oluşturulmuş bir obje(nesne). Onun bütün özelliklerini ve fonksiyonlarını barındırır.
yeniinsan.gozsayisi=2                       #İstersek bu objede ekstra özellikler ekleyebiliriz.
yeniinsan.gozrengi="mavi"                   #İstersek nesne içerisinde sınıftan kalıtılan değeri değiştirebiliriz.
print("Toplam göz: " + str(yeniinsan.gozsayisi))
print(yeniinsan.gozrengi)
print(yeniinsan.metot())




#ÖRNEK
class araba:
    kapisayisi=3
    renk="a"
    koltuksayisi=3

volvoaraba=araba()
volvoaraba.kapisayisi=4
volvoaraba.renk=["kırmızı","mavi"]
volvoaraba.koltuksayisi=5
print(volvoaraba.kapisayisi)

#ÖRNEK
class kutu:
    uzunluk = 0
    genislik = 0
    derinlik = 0
    def hacim(self):
        return self.uzunluk*self.genislik*self.derinlik     #Bu değerlerin nesne içerisinden alınması için başlarına self koymak zorundayım!!!

kutu1=kutu()
kutu1.uzunluk=5
kutu1.genislik=2
kutu1.derinlik=8
print(kutu1.hacim())




