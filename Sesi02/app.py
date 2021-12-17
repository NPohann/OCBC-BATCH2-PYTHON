# Conditioning in Python

x = 0
y = 5

if x < y:
    print('yes')

if y < x:
    print('yes')

if x:
    print('yes')

if y:
    print('yes')

if 'aul' in 'grault':
    print('yes aul')

if 'quux' in ['foo', 'bar', 'baz'] :
    print('yes foo')


z = 13
sunny = False
if z >= 10 and x <= 15 and not sunny:
    print(z)


hargaBuku = 20000
hargaMajalah = 5000
uang = 27000

if uang > hargaBuku:
    print('beli buku'); print("Hai")
elif uang > hargaMajalah:
    print("beli majalah")
else:
    print("uang tidak cukup")


# Conditional expressions
raining = True
print("Lets go to the", 'beach' if not raining else 'library')

# Looping
# n = 5
# while n > 0:
#     n-=1
#     print(n)

# i = 1
# while i < 6:
#     print(i)
#     i += 1

# Break & Continue Loop
# j = -1
# while j < 6:
#     print(j)
#     if j == 2:
#         break
#     j += 1

# print("print yang di luar loop")

# m = 5
# while m > 0:
#     m -= 1
#     if m == 2:
#         continue
#     print(m)
# print("Loop ended.")


# While else
m = 5
while m > 0:
    m -= 1
    print(m)
    if m ==2:
        break
print("Loop Done.")


# Loop FOR
dx = {'foo': 1, 'bar': 2, 'baz': 3}
for k, v in dx.items():
    print(k, ":", v)

# Range Loop
x = range(0, 10, 4)
for q in x:
    print(q)
