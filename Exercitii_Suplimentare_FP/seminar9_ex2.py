def main():
    bob = Student('bob')
    print(bob.name)
    bob.name = 'dob'

class Student:
    def __int__(self, name):
        object.__setattr__(self, "name", name)

    def __setattr__(self, name, value):
        raise ValueError()

    def __delattr__(self, name):
        raise ValueError()