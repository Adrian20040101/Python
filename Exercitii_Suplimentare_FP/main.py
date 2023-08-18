class Raum:
    def __init__(self, nummer, plaetze):
        self.nummer = nummer
        self.plaetze = plaetze
    def __str__(self):
        return f'Raum(nummer={self.nummer}, plaetze={self.plaetze})'
    def __eq__(self, other):
        return self.nummer == other.nummer


class Rechnerraum (Raum):
    def __init__(self, nummer, plaetze, os):
        super().__init__(nummer, plaetze)
        if os not in ('Windows', 'Linux', 'Unix', 'MACOS'):
            raise TypeError
        self.os = os
    def __str__(self):
        return f'Rechnerraum(nummer={self.nummer}, plaetze={self.plaetze})'

def main():
    r = Raum('2', 'Iorga')
    s = Rechnerraum('2', 'ceva', 'Windows')
    print (r)
    print(s)
    print (r==s)

main()