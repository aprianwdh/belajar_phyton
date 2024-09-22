print(10*"="+" PROGRAM MENENTUKAN GANJIL GENAP SUATU BILANGAN "+10*"=")
print(10*"="+" masukkan 0 jika sudah selesai "+10*"=")



while True:
    bilangan = int(input("masukkan bilangan = "))

    if bilangan <= 0:
        break

    if bilangan % 2 == 0:
        print("bilangan genap")
    else:
        print("bilangan ganjil")

print("program selesai")