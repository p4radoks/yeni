def asd(x):
    return x+15
print(asd(5))

#Def ile fonskiyon oluşturuyoruz. fonksiyondaki değeri sonradan belirlemek için bekletiyoruz. Printde fonskiyonun ne yapacağını yazıyoruz.


def fonskiyon():                        #inputla x'i çekiyoruz.
    x=input("x'in değerini yazın:")
    return pow(int(x),4)+3*int(x)+25
print("x'e göre sonuç: " + str(fonskiyon()))





def ismin_ne():
    isim = input("ismin ne? ")
    return isim
print("Merhaba {}. Nasılsın?".format(ismin_ne()))





