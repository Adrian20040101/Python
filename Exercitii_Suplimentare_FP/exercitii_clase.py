# class Raum:
#     def __init__(self,nummer,platze):
#         self.nummer = nummer
#         self.platze = platze
#     def __eq__(self, other):
#         return self.platze == other.platze
#     def __gt__(self, other):
#         return self.nummer >= other.nummer
#     def __lt__(self, other):
#         return self.platze <= other.platze
#     def __add__(self, other):
#         return self.platze + other.platze
#     def __str__(self):
#         return f'Room {self.nummer} has a total of {self.platze} places'
#
# class Rechnerraum(Raum):
#     def __init__(self,nummer,platze, OS):
#         super().__init__(nummer,platze)
#         self.OS = OS
#         if OS not in ('Windows', 'Linux', 'Unix', 'MacOS'):
#             raise TypeError
#     def __str__(self):
#         return f'Room {self.nummer} has a total of {self.platze} places and each PC in this room runs on {self.OS}'
#
#
# def main():
#     raum = Raum("173", 230)
#     raum2 = Raum('145', 200)
#     print(raum)
#     print(raum2)
#     print ("No. of places from the two rooms is :")
#     print(raum + raum2)
#     rr = Rechnerraum("149", 300, "Windows")
#     print(rr)
# main()

# class Animal:
#     def __init__(self, name):
#         self.name = name
#     def eat(self):
#         return f'{self.name} is eating...'
#
# class Pig(Animal):
#     def __init__(self, name, age):
#         super().__init__(name)
#         self.age = age
#     def sleep(self):
#         return f'{self.name} is sleeping...'
#
# class Chicken(Animal):
#     def __init__(self, name, color):
#         super().__init__(name)
#         self.color = color
#
# class Farm:
#     def __init__(self, animals, name, city):
#         self.animals = animals
#         self.name = name
#         self.city = city
#     def feedAnimals(self):
#         for animal in self.animals:
#             print(animal.eat())
#
# def main():
#     farm = Farm([Pig('bob', 4), Chicken('rob', 'yellow')], 'Cluj Farm', 'Cluj')
#     farm.feedAnimals()
# main()

class Building:
    def __init__(self):
        self.rooms = []
    def add_rooms(self,rooms):
        for room in rooms:
            self.rooms.append(room)
    def filter_rooms(self):
        return [room for room in self.rooms if room.places % 2 == 0]
    def delete_rooms(self, room):
        self.rooms.remove(room)
    def sort_rooms(self):
        self.rooms.sort(key = lambda x : x.places, reverse=True)
    def show_rooms(self,rooms):
        for room in rooms:
            return room

class Room:
    def __init__(self, number, places):
        self.number = number
        self.places = places
    def update_rooms(self, new_places):
        self.places = new_places

    def __str__(self):
        return f"{self.number}: {self.places}"

building = Building()
r1 = Room("125", 100)
r2 = Room("159", 140)
r3 = Room("209", 80)

building.add_rooms([r1,r2,r3])
print(building.show_rooms([r1,r2,r3]))



print (r1.places)
r1.update_rooms(120)
print(r1)
