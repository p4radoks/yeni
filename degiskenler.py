#Not Hesaplama

a = input("Vize Girin: ")
vize = int(a)                   #a değikenin ekrandan aldığı değer başlangıçta string. Onu inte çevirmek için int(b) kullanıyoruz.
b = input ("Final Girin: ")
final = int(b)

sonuc = vize*0.3 + final*0.7

print (sonuc)



c = 8
d= str(c)           #c değişkeninin aldğı değer int. string ifadeye dönüştürmek için str(c) kullanıyoruz.
print(d)


e = input("sayiyi girin: ")     #bu şekilde print içerisinde de tip değiştirme yapılabilir. Ekstra atama yapmamıza gerek kalmaz böylece
f = input("sayiyi girin: ")
print (int(e) + int(f))



