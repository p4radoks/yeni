#metot.fonskiyon

isim=["ahmet","mehmet","barış"]
isim.append("seyfi")     #append(ekleme) fonskiyonu ile diziye yeni bir isim ekledik.
print(isim)

sayi1=[1,2,3,3,3,3,4,4,5]
print(sayi1.count(3))    #dizimizin içerisinde kaç tane 3 olduğunu gösteren fonksiyon
print(sayi1.count(8))

sayi2=[8,9,10]
sayi1.extend(sayi2)      #sayi1 dizisini sayi2 dizisi ile genişlettik. sayi1 dizisine sayi2 dizisini ekledi.  sayi1+sayi2 gibi
print(sayi1)

print(sayi1.index(8))   #bize 8'in dizi içerisinde nerede olduğunu gösterir.

sayi1.insert(2, 8)      #Dizideki 2. sıraya 8 sayısını yerleştirdik
print(sayi1)


print(sayi1.pop(2))     #Diziden 2. sayıyı bize göstererek siler.
print(sayi1)

print(sayi1.remove(3))  #Remove da popla aynı işlemi yapar fakat; İndexi değil sileceğimiz değeri yazmalıyız. Ayrıca pop'da silmeden görebiliriz ama remove da göremeyiz.
print(sayi1)

sayi1.reverse()         #Listeyi tersten yazdırır. (Print içinde olmuyor bu fonksiyon)
print(sayi1)



