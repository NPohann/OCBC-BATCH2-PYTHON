# Fungsi untuk convert suhu kelvin ke celcius
def KtoCConverter(temperature):
    "Function for converts kelvin temperature into celcius temperature"
    return temperature - 273.15

# Fungsi untuk convert suhu celcius ke kelvin
def CtoKConverter(temperature):
    "Function for converts celcius into kelvin temperature"
    return temperature + 273.15

# Fungsi untuk convert suhu kelvin / celcius ke farenheit
def CKtoFConverter(temp, amount):
    "Function for converts celcius or kelvin into farenheit temperature"
    if temp == "C" or temp == "c" :
        return (amount*9/5)+32
    elif temp == "K" or temp == "k":
       convertion = KtoCConverter(amount) # Memanggil fungsi convert kelvin to celcius karena mekanisme yg sama
       return (convertion*9/5)+32
    else :
        return "The Temperature is unknown"

# Fungsi untuk convert suhu farenheit ke kelvin / celcius
def FtoCKConverter(temp, amount):
    "Function for converts farenheit into celcius or kelvin temperature"
    if temp == "C" or temp == "c":
        return (amount-32)*5/9
    elif temp == "K" or temp == "k":
        return (amount-32)*5/9+273.15


print("========== ASSIGNMENT 2 ==============")

print("======== Temperature Converter ==============")

menu = True

# Interactive Menu untuk memilih fungsi converter
while menu == True:
    print("1. Kelvin to Celcius")
    print("2. Celcius to Kelvin")
    print("3. Kelvin / Celcius to Farenheit")
    print("4. Farenheit to Kelvin / Celcius")
    choice = int(input("Choose your menu : "))

    if choice == 1: 
        print("Kelvin to Celcius Converter")
        k = float(input("Input your temperature amount : "))
        convertion = KtoCConverter(k)
        print(f"{k}° Celcius has the same amount with {convertion}° Kelvin")
    elif choice == 2:
        print("Celcius to Kelvin Converter")
        c = float(input("Input your temperature amount : "))
        convertion = CtoKConverter(c)
        print(f"{c}° Kelvin has the same amount with {convertion}° Celcius")
    elif choice == 3:
        print("Kelvin / Celcius to Farenheit Converter")
        temp = str(input("What temperature you want to convert? (C/K) "))
        amount = float(input("Input your temperature amount : "))
        convertion = CKtoFConverter(temp, amount)
        print(f"{amount}° {temp} has the same amount with {convertion}° Farenheit")
    elif choice == 4:
        print("Farenheit to Celcius / Kelvin Converter")
        temp = str(input("What temperature you want to convert into? (C/K) "))
        amount = float(input("Input your temperature amount : "))
        convertion = FtoCKConverter(temp, amount)
        print(f"{amount}° Farenheit has the same amount with {convertion}° {temp}")
    else:
        print("Choose the right menu!")

    loop = str(input("Choose other menu? (Y/N) ")) # Looping untuk mengulang pemilihan menu
    if(loop == "Y" or loop == "y"):
        menu = True
    else:
        menu = False
        print("==================THANK YOU===================")
