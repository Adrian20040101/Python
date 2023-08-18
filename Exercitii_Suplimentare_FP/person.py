class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def eat(self):
        print(f'{self.name} is eating...')
    def __str__(self):
        return f'Person(name={self.name}, age={self.age})'
    def __eq__(self, other):
        return self.name == other.name and self.age == other.age
"""
Person = Bassisklasse, Oberklasse, Superklasse
Student = Unterklasse
Student vererbt alle Methoden und alle Attribute von Person (name, age) + die eat Methode
Student kann weitere Methoden definieren und implementiere (study Methode)
is-a Beziehung zwischen 2 Objekten (Student und Person)
method overloading = x Methoden mit den gleichen Namen aber mit unterschiedlichen Parametern (not in python)
method overriding = die gleiche Methode (Name und Parameters) in beiden Klassen (Unterklasse und Superklasse) hat, aber mit unterschliedischen implementiereung
"""

class Student(Person):
    def __init__(self, name, age, uni):
        super().__init__(name, age) #die __init__ methoder der Superklasse aufgerufen, um name und age initialisieren zu koenen
        self.uni = uni
    def study(self):
        print(f'{self.name} ist studying...')
    #overriding
    def eat(self):
        print(f'{self.name} cannot eat....must study...')
    def study (self, course):
        print(f'{self.name} is studying for {course}')

def add():
    return 1 + 2
def add(a, b):
    return a + b
def main():
    print(add(1,2))
    bob = Person('bob', 20)
    bob.eat()
    dob = Student('dob', 21, 'ubb')
    dob.study('Python')
    dob.eat()
    print(bob)
    zob = Person('zob', 21)
    #print (zob == bob) #zob.__eq__(bob) => zob = self, bob = other
    print (bob == zob) #zob.__eq__(bob) => bob = self, zob = other
main()
