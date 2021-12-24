# Python OOP
# raka = ["Raka Ardhi", 28, "CurDev", 2265]
# spock = ["Spock", 35, "Science Officer", 2254]
# mccoy = ["Leonard McCoy", "Chief Medical Officer", 2266]

# print("Daftar nama : ", raka[0], spock[0], mccoy[0])
# print("Daftar umur : ", raka[1], spock[1], mccoy[1])
# print("Daftar jabatan : ", raka[2], spock[2], mccoy[2])
# print("Daftar tahun mulai : ", raka[3], spock[2], mccoy[3])

# Class in Python
class Dog:
    species = "Canis familiaris"
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def description(self):
            return f"{self.name} is {self.age} years old"

    def speak(self, sound):
            return f"{self.name} says {sound}"


# dog_1 = Dog("Miley", 9) # _init_(dog_1, "Miley", 9)
# dog_2 = Dog("Hike", 2)  # _init_(dog_2, "Hike", 2)

        
# print(dog_1.name, dog_1.age)
# print(dog_2.name, dog_2.age)

# dog_3 = Dog("Scooby", 1)
# print(dog_3.name, dog_3.age)

# print("Species")
# print(dog_1.species)
# print(dog_2.species)
# print(dog_3.species)

# print(dog_1.speak("Woof woof"))
# print(dog_2.description())

miles = Dog("Miles", 4, "Jack Russell Terrier")
buddy = Dog("Buddy", 9, "Dachshund")
jack = Dog("Jack", 3, "Bulldog")
jim = Dog("Jim", 5, "Bulldog")


# Subclass of Dog
class Bulldogs(Dog):
    def speak(self):
        return f"{self.name} says Woof Woof"

# Subclass of Dog
class Dachshund(Dog):
    def speak(self):
        return f"{self.name} says Yap"

class JackRusselTerrier(Dog):
    pass

hike = Bulldogs("Hike", 9, "Bulldogs")
miles = JackRusselTerrier("Miles", 4, "JackRusselTerrier")

print(hike.speak())
print(miles.speak("Arf"))