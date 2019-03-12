dizi1=[1,3,5]
dizi2=[2,4,6]
dizi3=["ahmet","mehmet","ali","seyfullah","kerem"]
isim= "barış"
print(dizi1 + dizi2)
print(isim)

# print(dizi1 + isim)  dizimiz sayılardan oluştuğu için string bir ifade ile yazdıramıyoruz.

print('Merhaba '*10) #Ekrana 'Merhaba 'yuı 10 kere yazdırma

print(1 in dizi1) #dizi1'in içinde 1 var mı diye kontrol etme True ise var False ise yok.
print(2 in dizi1)
print("selim" in dizi3)

print('b' in isim) #string ifadeler için de kullanabiliriz "barış" kelimesinin içinde 'b' harfi var mı diye kontrol etti
print('c' in isim)


dizi4=[8,5,7,45,444,245,15245,-155]
print(len(dizi4))               #dizinin uzunluğunu verir.
print(max(dizi4))               #dizideki sayıca en büyük değeri verir.
print(min(dizi4))               #dizideki sayıca en küçük değeri verir.

#print(max(dizi3))                 BU BÖLÜMLER SORULACAK
#print(min(dizi3))

dizi4[3]=8  #dizideki herhangi bir değeri değiştirme istediğimde kullanırız. 0'dan başlamayı unutma!!!!
print(dizi4)

del dizi4[3]    #diziden eleman silme
print(dizi4)

print(list(dizi3[4])) #dizi3'ün 4. dizisindeki 'kerem' elementenini karakterlerinin gösterimi
