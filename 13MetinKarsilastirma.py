metin1=("jadfgkladlşigaowerjgamdfgjarıvıamdırg")
metin2=("sladgjadilfmviaoperkagödlfvkadrkoadöflvasöef")

fark=""

for karakter in metin1: #metin 1 deki her karakteri karaktere atadı.
    if not karakter in metin2:  #eğer metin2'de metin1'den çektiği karakter yoksa
        if not karakter in fark:    #eğer farkta da metin1'den çekilen karakter yoksa
            fark+=karakter          #karakter stringinin içindeki değeri fark'a ekle
print(fark)


#Yukarıdaki döngünün doğruluğunu kontrol amaçlı
print(metin1.index("ş"))
print(metin1.index("w"))
print(metin1.index("ı"))

#print(metin2.index("ş"))   Bu bölüm çalışmıyor çünkü metin2 içerisinde bu karakterler yok!
#print(metin2.index("w"))
#print(metin2.index("ı"))