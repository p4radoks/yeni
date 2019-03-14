Aile={"baba":"Ahmet","anne":"Yasemin","kardes":"Mehmet"}    #İlk değer anahtar kelime. İkincisi ise bu anahtar kelimeye bağlı değer.
print(Aile["baba"])             #Print ile anahtar kelimeyi yazdığımda ona bağlı değer ekrana yazdırılır.

yas={"baba":42,"anne":65}
print(yas["baba"])

yas1=yas.copy()     # yas sözlüğünün içerisindeki bütün değerleri aynen kopyalama
print(yas1)








Aile.clear()                    #Dictionary içindeki bütün anahtar kelime ve değerleri siler.
print(Aile)