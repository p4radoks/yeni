import ImportIcınFonksiyon                       #ImportIcınFonksiyon adlı dosyayı bu dosyaya import ettim. İçindekiher şey artık bu dosyada da var
class iki:                                       #Çektiğim dosya içerisindeki fonksiyonda herhangi bir değişiklik yaparsam değişiklik direk uygulanır.
    def asd(self):
        return ImportIcınFonksiyon.merhaba()    #Import ettiğim dosya içerisindeki fonksiyonu döndürmek için önce çektiğim dosya adı, sonra fonksiyon adını yazdım.


yepyeni=iki()
yepyeni.asd()




kalem=ImportIcınFonksiyon.merhaba()              #İstersek bu şekilde import ettiğimiz dosyadaki fonksiyonu çalıştırmak için herhangi bir objeye atayabiliriz.

#PYTHON TERMİNALDE İMPORT EDİLEN DOSYADAKİLERİN DEĞİŞTİRİLMESİ HALİNDE RELOAD İLE YENİDEN İMPORT ETMEK GEREK.

import math
print(dir(ImportIcınFonksiyon))                 #dir modül içerisinde neler olduğunu görmek için kullanılır.
print(help(ImportIcınFonksiyon))                #help kullanabileceğin fonksiyonların kullanımını gösterir. Detaylı gösterimdir.
print(help(math))
print(math.__doc__)                             #math ile ne yapabileceğimi yazar. Özet niteliğinde.


