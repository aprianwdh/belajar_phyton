import os
os.system("cls")

saldo = 100
deposit = 0
print(10*"="+"SELAMAT SATANG"+10*"=")
print(10*"="+"ATM WAKANDA"+13*"="+"\n")


print("1.Cek Saldo")
print("2.Deposit : ")
print("3.Tarik Saldo : ")
print("4.Keluar : \n")

while(True):
    pilihan = str(input("masukkan piihan anda = "))

    if pilihan == "1":
        print(f'saldo anda : Rp.{saldo}\n')
        continue
    elif pilihan == "2":
        deposit = int(input('masukkan nominal = Rp.'))
        print(f"deposit senilai {deposit}\n")
        saldo += deposit
        continue
    elif pilihan == "3":
        tarik = int(input("masukkan nominal yang inin ditarik = Rp."))
        if tarik>saldo:
            print("saldo kurang tidak bisa menarik uang ygy\n")
        elif tarik<=saldo:
            saldo -= tarik
            print("berhasil ygy\n")
        continue
    elif pilihan == "4":
        print("keluar....")
        break
    else:
        print("pilihan salah ygy")
        continue

