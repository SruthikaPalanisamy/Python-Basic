class Animal:
    def __init__(self , name , sound):
        self.name = name
        self.sound = sound
    def speak(self):
        print(f"The {self.name} says {self.sound}")
    

class Dog(Animal):
    def speak(self ):
        print(f"the Dog will bark bow 🐕‍🦺🦴")


class Cat(Animal):
    
    def speak(self):
        print(f"the Cat will say meow meow ")


cuckoo = Animal("cuckoo" , "singg")
cuckoo.speak()
Donkey = Animal("Donkey" , "Shout")
Donkey.speak()
Cow = Animal("Cow" , "Scream")
Cow.speak()

c = Dog("Dog", "Bow")
c.speak()
d = Cat("Cat", "Meow")
d.speak()