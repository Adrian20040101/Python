# Schreiben Sie eine Funktion, die die Summe aller geraden Ziffer einer angegebenen Zahl berechnet.

def sum(number):
    if number == 0:
        return 0
    else:
        last_digit = number % 10
        if last_digit % 2 == 0:
            return last_digit + sum(number // 10)
        else:
            return sum(number // 10)
print(sum(46792))

# Schreiben Sie eine Funktion, die den letzten erhaltenen Großbuchstabe der Zeichenkette zurückgibt.

def find_last_capital(string):
    if len(string) == 0:
        return None
    elif string[-1].isupper():
        return string[-1]
    else:
        return find_last_capital(string[:-1])
print(find_last_capital("jdnsDdenfjNhdwbSd"))


# Schreiben Sie für eine gegebene Zeichenkette eine Funktion,die die Gesamtzahl der darin enthaltenen Vokalen (a, e, i, o und u) zählt.

def count_vowels(string):
    vowels = "aeiouAEIOU"
    if len(string) == 0:
        return 0
    elif string[0] in vowels:
        return 1 + count_vowels(string[1:])
    else:
        return count_vowels(string[1:])
print(count_vowels("hdbenaneki"))

# Schreiben Sie für eine Zahl eine Funktion, die true zurückgibt, wenn die angegebene Zahl Palindrom ist, andernfalls falsch.

def is_palindrome(num):
    if num < 0:
        return False
    if num < 10:
        return True
    return str(num) == str(num)[::-1]  #reversing the string of number
print (is_palindrome(112211))

# Schreiben Sie eine Funktion, die das größte Element einer Liste zurückgibt.

def find_biggest(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        return max(lst[0], find_biggest(lst[1:]))
print(find_biggest([1, 4, 6, 2, 3, 7, 8, 3]))

# Schreiben Sie eine Funktion,die prüft,ob eine Zahl in einer Liste erhalten ist. Jedes Element kann entweder eine Liste oder eine Zahl sein

def verify(list, x):
    if len(list) == 0:
        return False
    if list[0] == x:
        return True
    return verify(list[1:], x)

print(verify([1, 5, 6, 3, 8, 2], 8))

# Schreiben Sie eine Funktion, die die Summe der Elemente einer Liste berechnet. Jedes Element kann entweder eine Liste oder eine Zahl sein.

def suma(list):
    if len(list) == 0:
        return 0
    else:
        return list[0] + suma(list[1:])

print(suma([1, 3, 4, 5, 7, 1, 2]))


#----------------------------------------------------------------------------------------------------------------------------------

def gerade(number):
    if number == 0:
        return 0
    else:
        last_digit = number % 10
        if last_digit % 2 == 0:
            return last_digit + gerade(number // 10)
        else:
            return gerade(number // 10)

print(gerade(185429))

def capital(string):
    if len(string) == 0:
        return 0
    else:
        if string[-1].isupper():
            return string[-1]
        else:
            return capital(string[:-1])
print(capital("jdjenDHdejDjdneLdEs"))

def count_vowels(string):
    if len(string) == 0:
        return 0
    else:
        if string[0] in "aeiouAEIOU":
            return 1 + count_vowels(string[1:])
        else:
            return count_vowels(string[1:])
print(count_vowels("debjkdehbdnkdeu"))

def pailndrome(number):
    if number < 0:
        return False
    elif number < 10:
        return True
    else:
        if str(number) == str(number)[::-1]:
            return True
    return False

print(pailndrome(112211))

def summe(number):
    if number == 0:
        return 0
    else:
        last_digit = number % 10
        return last_digit + summe(number // 10)

print(summe(123456))

def smallest(list):
    if len(list) == 0:
        return 0
    elif len(list) == 1:
        return list[0]
    else:
        return min(list[0], smallest(list[1:]))
print(smallest([2,5,3,6,8,3,9]))

def power(a, b):
    if a == 0:
        return 0
    elif b == 0:
        return 1
    else:
        return a * power(a, b - 1)
print(power(3, 3))

def string_palindrome(string):
    if len(string) == 0:
        return 0
    else:
        if string == string[::-1]:
            return True
        else:
            return False
print(string_palindrome("abcddcba"))

def first_capital(string):
    if len(string) == 0:
        return 0
    else:
        if string[0].isupper():
            return string[0]
        else:
            return first_capital(string[1:])

print(first_capital("djndSjdnjenDhdbCdndEn"))

def is_sorted(list):
    if len(list) == 0:
        return 0
    elif len(list) == 1:
        return True
    else:
        return list[0] <= list[1] and is_sorted(list[1:])

print(is_sorted([3, 5, 6, 7, 9]))

def reverse(string):
    if len(string) == 0:
        return 0
    elif len(string) == 1:
        return string[0]
    else:
        return reverse(string[1:]) + string[0]
print(reverse("abcdefg"))