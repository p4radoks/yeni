fob=open("/home/p4radoks/Desktop/a.text","w")       #Çalıştırdığım zaman masaüstüne a.text dosyasını oluşturdu.      w burada yazma manasına geliyor.
fob.write("Merhaba DÜnya\n"
          "Sana da merhaba\n")                          #Açılan bu belgenin içerisine "Merhaba Dünya" yazıldı.
fob.write("Günaydın")
fob.close()                                         #Ardından close ile dosyaya yazmayı kapattık.

fob=open("/home/p4radoks/Desktop/a.text","r")       #Dosyayı okuma halinde açtık.
print(fob.read(3))                                  #İlk 3 harfi okuduk.
print(fob.read())                                   #Ardından geriye kalanları okuduk. İlk 3 harfi bir önceki satırda okuduğumuz için onları okuyamıyoruz.
print(fob.read())                                   #Diğer satırlarda hepsini okuduk o yüzden hiçbir şey okuyamıyoruz.
fob.close()


fob=open("/home/p4radoks/Desktop/a.text","r")
print(fob.readline())                               #Sadece tek bir satırı okur.
listme=fob.readlines()                              #readlines Bütün satırları okur. Liste şeklinde gösterir. #İstersek readlines ı bir list e atayıp daha sonra o listede değişiklikler yapabiliriz.
fob.close()

listme[1]="Merhaba yeni yeni dünya"
print(listme)

fob=open("/home/p4radoks/Desktop/a.text","w")
fob.writelines(listme)                              #İstersek bu şekilde liste içerisinde değiştirdiklerimizi dosyaya aktarabiliriz.
fob.close()