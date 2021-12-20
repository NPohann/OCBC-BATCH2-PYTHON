# try:
#     file = open("Hack8_sample_text.txt", encoding = "utf-8")
# f = open("Hack8_sample_text.txt", "w") #Write => Menulis dan replace existing text
# f = open("Hack8_sample_text.txt", "a") #Append => menambahkan item di akhir text
# f = open("Hack8_sample_text.txt" "r") #Read => membaca text
# finally:
#     file.close()

# with open("text.txt", "w", encoding = "utf-8") as f:
#     f.write("my first file\n")
#     f.write("this file\n\n")
#     f.write("contains three lines\n")


# file = open("Hack8_sample_text.txt")
# print(file.read(6))
# print(file.read())
# print(file.tell())
# file.close()

file = open("Hack8_sample_text.txt")
file.seek(0)
# for line in file:
#     print(line, end = '')
# print(file.readline())
# print(file.readlines())

# x = 10
# if x > 5:
#     raise Exception("x Shouldnt be more than 5")

# import sys
# assert('windows' in sys.platform), "This code runs on windows only."

# x = 22
# assert x == 20, "x harus 20"

def perkalian_dengan_0(num1):
    return 0 * num1 + 1

a = 0

sepuluh_kali_0 = perkalian_dengan_0(10)
assert sepuluh_kali_0 == 0, "Fungsi masih salah"