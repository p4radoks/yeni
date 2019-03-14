cumle="Bugün günlerden %s"          # %s yerine daha sonradan belirttiğimiz herhangi bir şeyi koyabiliriz
varb=("pazartesi")
varc=("pattes")
print(cumle % varb)
print(cumle % varc)

print(cumle.find("günlerden"))      # Cümle içerisindeki "günlerden" kelimesinin nereden başladığını bulmaya yarar.

dizi1=["ahmet","mehmet","cafer"]
isim1="selim"
print(isim1.join(dizi1))            #Dizinin içerisindeki her değerin arasına "selim"i sokar. dizi1 ya da isim1 içeriğini değiştirmez. Sadece printte kullanılıyor.
isim2=isim1.join(dizi1)             #İstersek bu şekilde atama yapabiliriz.
print(isim2)

cumle2="BUGÜN ben Derse GİTtim."    #Cümle içerisindeki bütün karakterler küçük harfe dönüştü.
print(cumle2.lower())

cumle3="Bugün ben derse gitmedim."  #Replace ile cümle içerisindeki herhangi bir kelimeyi başka bir kelime ile değiştirebiliriz.
print(cumle3.replace("gitmedim","gittim"))



