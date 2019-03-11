aile = ["ahmet", "mehmet", "cafer", "selim", "barış", "deniz", "hüseyin", "karamel"]  #diziler 0'dan başlar. Eğer tersten başlatacaksak -1'den başlar.
print(aile[2])
print(aile[-1])

print("ahmet"[3])  #bu şekilde herhangi bir string ifadenin karakterlerini de dizi gibi kullanabiliyoruz.

print(aile[1:5])   #Bu şekilde 1.'den 5.'ye kadar listeler (5 dahil değildir)

print(aile[-5:])   #-5'ten başlayarak son değere kadar gider. [-5:0] yapılmaz!!!! Yapılırsa boş bir değer verir.

print(aile[:5])    #0'dan başlayak 5'e kadar gider. (5 dahil değil)

print(aile[:])      #bütün diziyi gösterir.

print(aile[1:8:3])  #3. parametre kaç tane atlayacağını gösterir. Yani 1'i aldıktan sonra 4'ü alır. Sonra 7'yi alır.

print(aile[8:0:-2]) #Geriye doğru 2 atlayarak gösterir.
print(aile[::-2])   #Yukarıdaki ile aynı işlemi yapar (7'den başlar)
print(aile[::2])    #Yukarıdakinin pozitif hali (0'dan başlar)
