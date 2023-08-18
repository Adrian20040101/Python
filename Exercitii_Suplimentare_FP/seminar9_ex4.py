class Raum:
    def __init__(self, name, platze):
        self.name = name
        self.platze = platze

class Gebaude:
    def __init__(self, raume):
        self.raume = raume

def main():
    r1 = Raum('unu', 100)
    r2 = Raum('doi', 200)
    g = Gebaude([r1, r2])

main()