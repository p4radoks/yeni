vize = input("Lütfen vize notunu girin: ")
final = input("Lütfen final notunu girin: ")
ort = int(vize) * 0.3 + int(final) * 0.7

if ort >= 60:
    if ort >= 60 and ort <= 64:
        print("CC ile geçtin!")
    elif ort >= 65 and ort <= 69:
        print("CB ile geçtin!")
    elif ort >= 70 and ort <= 79:
        print("BB ile geçtin!")
    elif ort >= 80 and ort <= 89:
        print("BA ile geçtin!")
    elif ort >= 90 and ort <= 100:
        print("AA ile geçtin!")
elif ort < 60 and ort >= 50:
    print("Ortalaman 2.50 ise DD ile geçtin!")
elif ort >= 30 and ort <= 49:
    print("FD ile kaldın")

else:
    print("FF ile kaldın!")







if ort>60 or ort<50:        #Ortalama 60'dan büyükse ya da 50'den küçükse demektir. (50-60 arası else'e girer.)
    print("Or")
else:
    print("Bu aralıklarda değil")

#NOT : Harf notu hesaplamayı üni sitesinden aldım. O nedenle 69.75 ya da 79,63 not ortalamasına herhangi bir değer döndürmüyor.

