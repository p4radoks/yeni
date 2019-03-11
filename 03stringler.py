
print ("Ahmet")   #İçeride tırnak kullanımı olmadığı sürece tek ve çift tırnak arasında fark yok
print ('Ahmet')
print ("Ahmet'in amcası")    #Eğer içeride tek tırnak kullanılacaksa dışarıda çift tırnak kullanılmalı. Dışarıda tek tırnak kullanılırsa çalışmaz.
print ("Ahmet bana dedi ki: \"Ben de Ahmet'le gelmek istiyorum\"")   # \ işareti kendinden sonra gelen işaretin aslında varolan fonksiyonda çalışmadığını belirtir.

print ("Ahmet bana dedi ki: "Ben de gelmek istiyorum" ")   #Kodun bu hali çalışmaz!  İçeride ve dışarıda çift tırnak olmaz!

a = "Ahmet "
b = "KAPLICA"
print (a+b)



sayi1 = 18
print ("Ahmet'in yaşı: " + str(sayi1)) # string bir ifade ile int değeri + diyerek aynı print içerisine yazdıramıyoruz. Bu nedenle sayi1 ifadesini string bir değere dönüştürdük.

print ("Ahmet'in yaşı: " + 'sayi1') # videoda göstermesine rağmen bu şekilde çalışmıyor!!!!



