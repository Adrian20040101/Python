# ex1/L2
# Enfernen Sie die Zahlen die sich wiederholen.

def ex1():
    l = [23, 32, 45, 67, 12, 12, 34, 67, 12, 34, 54, 31]
    rez = []
    for i in range(0, len(l)):
        ct = 0
        for j in range(i + 1, len(l)):
            if l[i] == l[j]:
                ct = ct + 1
        if ct == 0:
            rez.append(l[i])
    print(rez)


# ex1()

# ex2/L2
# Schreiben Sie die Anzahl von symmetrischen Paaren (xy) und (yx).

def ex2():
    l = [23, 32, 45, 67, 21, 34, 12, 34, 76, 31]
    ct = 0
    for i in range(0, len(l) - 1):
        for j in range(i + 1, len(l)):
            aux = l[j]
            inv = 0
            while aux > 0:
                inv = inv * 10 + aux % 10
                aux = int(aux / 10)
            if (inv == l[i]):
                ct = ct + 1
    print(ct)


# ex2()

# ex3/L2
# Generieren Sie die größte möglicheZahl, die aus der Konkatenation der Elemente der Liste gebildet ist.

def ex3():
    l = [23, 32, 45, 67, 21, 34, 89, 34, 76, 31]
    nr = 0
    l.sort(reverse=True)  # sortiert in fallender Reihenfolge
    # l.sort() #sortiert in steigender Reihenfolge
    for i in range(0, len(l)):
        nr = nr * 100 + l[i]
    print(nr)


# ex3()

# ex6/L2
# Finden Sie die längste zusammenhängende Domino Teilfolge

def ex6():
    l = [34, 56, 64, 23, 48, 87, 76, 69, 91, 12, 45]
    temp = []
    rez = []

    def domino(a, b):
        b = b // 10  # so erhalt man die ganze Zahl un nicht eine rationale Zahl
        if a % 10 == b % 10:
            return True
        return False

    for i in range(0, len(l) - 1):
        if domino(l[i], l[i + 1]):
            temp.append(l[i])
        elif len(temp) > len(rez):
            temp.append(l[i])
            rez = temp
            temp = []
    if len(temp) > len(rez):
        # temp.append(a)
        rez = temp
    # temp = []
    print(rez)


# ex6()
# Verschlüsseln  Sie  die  Elemente  der  Liste
def ex4():
    l = [12, 34, 56, 78, 36, 23]
    key = l[0]
    new_list = []
    new_list.append(l[0])
    for i in range(1, len(l)):
        l[i] = l[i] + key
        new_list.append(l[i])
    print(new_list)


# ex4()

# Finden Sie den kleinsten gemeinsamen Vielfachen zwischen Index fromund to
def ex7():
    l=[23,45,67,21,24,12,34]

    def cmmdc(x, y):
        x = abs(x)
        y = abs(y)
        while x != y:
            if x > y:
                x -= y
            else:
                y -= x
        return x


    def cmmmc(x, y):
        return x * y // cmmdc(x, y)

    index1= int(input("Indexul initial este: "))
    index2= int(input("Indexul final este: "))


    for i in range (0,len(l)):
        if index1<0 or index1>len(l)-1 or index2<1 or index2>len(l):
            print ("Index out of range")
            break
        else:
            k = l[index1+1]
            for i in range(index1+1, index2):
                k = cmmmc(k, l[i + 1])
            print (cmmmc(l[index1],l[index2]))
            break
#ex7()

#Filtern Sie die Zahlen, die eine bestimmte Beziehung zwischen Zahlen haben, die in einem String angegeben wird.(z.B:“x=y*3”, “x/y=2“, ...)
def ex5():
    def result_from_side_operation(formula_side, a, b):
        if "*" in formula_side:
            result = a * b
        elif "/" in formula_side:
            result = a // b
        elif "-" in formula_side:
            result = a - b
        else:
            result = a + b

        return result

    def filter_numbers(numbers_list, formula_string):
        filtered_numbers = []

        # Impart string formula in doua parti
        # ex: formula = "3*x=y/3" devine ["3*x", "y/3"]
        formula_sides = formula_string.split("=")

        original_left_side = str(formula_sides[0]).rjust(3,"0")
        original_right_side = str(formula_sides[1]).rjust(3,"0")

        print(f"left side: {original_left_side}")
        print(f"right side: {original_right_side}")
        print(30 * "-")

        # Fac operatiile pentru toate numerele din lista
        for number in numbers_list:
            # pentru 31 va fi x = 3 y = 1
            x = number // 10
            y = number % 10

            # Aici se va reveni la formula originala
            # ex: "3*3" va redeveni 3*x in partea stanga
            # ex: "1/3" va redeveni "y/3" in partea dreapta
            left_side = original_left_side
            right_side = original_right_side

            # Inlocuiesc x si y din formula string cu valoarea lor
            # ex: "3*x" devine "3*3" cand numarul este 31
            if "x" in left_side:
                left_side = left_side.replace("x", str(x))
            else:
                right_side = left_side.replace("x", str(x))

            # ex "y/3" devine "1/3" cand numarul este 31
            if "y" in right_side:
                right_side = right_side.replace("y", str(y))
            else:
                left_side = left_side.replace("y", str(y))

            print(f"check: {left_side} = {right_side}")

                # Extrag valorile ca int din left_side si right_side

            left_first_value = int(left_side[0])

            left_second_value = int(left_side[2])

            right_first_value = int(right_side[0])

            right_second_value = int(right_side[2])

                # Salvez rezultatul operatiei facuta pe valorile extrase
            left_side_result = result_from_side_operation(left_side,
                                                              left_first_value,
                                                              left_second_value)

            right_side_result = result_from_side_operation(right_side,
                                                               right_first_value,
                                                               right_second_value)

                # Verific egalitatea cu valorile extrase din stringuri

            if left_side_result == right_side_result:

                filtered_numbers.append(number)

                print("true")
            else:
                print("false")

        print(30 * "-")
        print(f"filtered numbers: {filtered_numbers}")

    numbers = [31, 11, 39, 63, 19]

    # Formule pentru testare
    # formula = "x+2=y"
    # formula = "x=3*y"
    # formula = "x/y=2"
    # formula = "x-y=6"
    formula = "x=y"

    filter_numbers(numbers, formula)
ex5()