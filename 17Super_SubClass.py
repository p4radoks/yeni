class UstSinif:
    n1="Adım Barış"
    n2="Adım Mehmet"
class AltSinif(UstSinif):       #Alt sınıfımız üst sınıfta yer alan bütün niteliklere sahip.
    n3="Adım Murat"

ustnesne=UstSinif()
print(ustnesne.n1)
print(ustnesne.n2)

altnesne=AltSinif()
print(altnesne.n1)
print(altnesne.n2)
print(altnesne.n3)


#ÖRNEK

class Araba:            #Araba bizim üst sınıfımız
    kapi=0
    renk=""
    maxhiz=0
    yuzkmulasma=0

class Ford(Araba):      #Ford ise bizim alt sınıfımız. (Araba ile aynı niteliklere sahip ama model belirtme burada)
    kapi=4              #Eğer istersek bu şekilde nitelikleri değiştirebiliriz.
    #pass                Pass ile hiçbir şey yapmadan bu aşamayı geç diyoruz. Yani nitelik ya da fonksiyon atamadan class'ı oluşturduk.

mustang=Ford()
mustang.renk="mavi"
mustang.maxhiz=225
mustang.yuzkmulasma=3

print(mustang.kapi)




class Baba:
    n1="Merhaba ben baban :)"

"""
class Anne:                      Eğer bu şekilde her iki niteliği de n1'e atarsam cocuk sınıfımızın niteliği annedeki nitelik olur. O yüzden farklı niteliklere atamaya dikkat!
    n1='Merhaba ben annen.' 
"""

class Anne:
    n2="Merhaba ben annen."

class cocuk(Anne,Baba):
    n3="Merhaba ben çocuk."

yeninesne=cocuk()
print(yeninesne.n1)
print(yeninesne.n2)
print(yeninesne.n3)

