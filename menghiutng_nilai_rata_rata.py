print(10*"="+" Program Menghitung Nilai Rata Rata "+16*"=")
print(10*"="+" masukkan bilangan \'0\' jika sudah selesai "+10*"=")

jumlah_nilai = 0
i = 0

while True:
    nilai = float(input(f'masukkan nilai ke {i+1} = '))
    if nilai <= 0:
        break
    i += 1

    jumlah_nilai += nilai

    
nilai_rata_rata = jumlah_nilai / i

print(f"nilai rata rata = {nilai_rata_rata}")
