soru=("1-Toplama İşlemi"
            "\n2-Çıkarmak İşlemi"
            "\n3-Bölme İşlemi"
            "\n4-Çarpma İşlemi"
            "\n5-Programdan Çık ")
print(soru)
while 1:    #1 yerine True da yazabilirdik!
    islem1=input("Lütfen yapmak istediğiniz işlemin numarasını yazın:")
    if islem1=="5":
        print("Programdan çıkılıyor")
        break
    elif islem1=="1":
        sayi1=int(input("Birinci sayıyı girin: "))
        sayi2=int(input("İkinci sayıyı girin: "))
        print(sayi1, "+", sayi2, "=", sayi1+sayi2)
    elif islem1=="2":
        sayi1=int(input("Birinci sayıyı girin: "))
        sayi2=int(input("İkinci sayıyı girin: "))
        print(sayi1, "-", sayi2, "=", sayi1-sayi2)
    elif islem1=="3":
        sayi1=int(input("Birinci sayıyı girin: "))
        sayi2=int(input("İkinci sayıyı girin: "))
        print(sayi1, "/", sayi2, "=", sayi1/sayi2)
    elif islem1=="4":
        sayi1=int(input("Birinci sayıyı girin: "))
        sayi2=int(input("İkinci sayıyı girin: "))
        print(sayi1, "*", sayi2, "=", sayi1*sayi2)
    elif islem1=="5":
        print("Programdan çıkılıyor")
        break
    else:
        print("Lütfen belirtilen sayılardan birini girin!")
