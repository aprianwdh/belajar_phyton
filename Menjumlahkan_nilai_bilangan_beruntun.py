print(10*"="+" PROGRAM menjumlahkan nilai bilangan "+19*"=")
print(10*"="+" masukkan bilangan NEGATIF jika sudah selesai "+10*"=")

jumlah_bilangan = 0
i = 0

while True:
    bilangan = int(input(f"masukkan bilangan ke {i+1} = "))
    jumlah_bilangan += bilangan
    if bilangan <0:
        print('bilangan harus positif ya')
        continue
    elif bilangan == 0:
        break
    i+=1

    print(f'jumlah penjumlahan ke {i} = {jumlah_bilangan}')

print("program selesai")