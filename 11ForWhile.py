b=1
while b <=10:   #b 10 ya da 10'dan küçük ise döngü devam eder. Ve her döngüde b 1 artırılır.
    print(b)
    b+=1

dizi1=["ahmet","mehmet","cafer","selim"]    #for döngüsünde dizi1 içerisindeki her değer bizim için bir isim diye belirtiyoruz.
for isim in dizi1:
    print(isim)

yas1={"baba":42,"anne":52,"kardeş":25}      #burada sözlük içerisindeki değerleri döndürdük.
for yas in yas1:                            #sadece yas döndürürsek anahtar kelimeleri döndürür!
    print(yas, yas1[yas])

while 1:                                                                    #Burada eğer break olmazsa program sonsuz döngü içerisinde sürekli isim sorup duracak.
    isim=input("Lütfen isminizi yazın (0 yazarsanız programdan çıkar): ")   #Eğer ekrandan gelecek karakter "0" olursa program duracak.
    if isim == "0":                                                         #"0" burada döngüden çıkmanın anahtar kelimesi bir nevi
        break                                                               #Burada while'ın yanına 1 yerine True da yazabilirdik. Aynı işlevi görür.
    else:
        print(isim)






