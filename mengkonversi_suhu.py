print(10*"="+" PROGRAM mengkonversi suhu "+25*"=")
print(10*"="+" masukkan bilangan \'0\' jika sudah selesai "+10*"=")

while True:
    celcius = float(input("masukkan suhu damal celcius = "))

    if celcius == 0:
        break

    fahrenheit = (celcius * 9/5)+32
    kelvin = celcius + 273.15
    reamur = celcius * 4/5

    print(f'{celcius} C ---------> {fahrenheit} F')
    print(f'{celcius} C ---------> {kelvin} K')
    print(f'{celcius} C ---------> {reamur} R')

print("program selesai")