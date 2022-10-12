#Eiklida algoritms

#Алгоритм нахождения НОД вычитанием
a = int(input("a: "))
b = int(input("b: "))
while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a
print(a)
#Алгоритм нахождения НОД делением
c = int(input("c: "))
d = int(input("d: "))
while c != 0 and d != 0:
    if c > d:
        c = c % d
    else:
        d = d % c
print(c + d)