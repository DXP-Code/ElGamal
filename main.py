import random
import math


def CheckIfProbablyPrime(x):
    truthfulness = pow(2, x - 1, x) == 1
    if truthfulness == True:
        return "Число простое"
    else:
        return "Число не простое"


def rand_prime():
    while True:
        p = random.randrange(1501, 300000,
                             2)  # randrange - возвращает случайное целое число в заданном диапазоне, т.е. начало и конец.
        if all(p % n != 0 for n in range(3, int((pow(p, 0.5)) + 1), 2)):
            return p


def rand_primeK():
    while True:
        max = rand_prime()
        p = random.randrange(1501, max,
                             2)  # randrange - возвращает случайное целое число в заданном диапазоне, т.е. начало и конец.
        if all(p % n != 0 for n in range(3, int((pow(p, 0.5)) + 1), 2)):
            return p


def encryption(msg, p, y, g):
    ct= []
    a = pow(g,k,p)
    b = pow(y,k,p)
    for i in range(0,len(msg)):
        ct.append(msg[i])
    print("g^k= ", a)
    print("y^k= ", b)
    for i in range(0,len(ct)):
        ct[i]=b*(ord(ct[i])-1037)
    return ct, a


def decryption(ct, a, x, p):
    pt=[]
    h=pow(a,x,p)
    for i in range(0, len(ct)):
        pt.append(chr(int((ct[i]/h)+1037)))
    return pt

while True:
    choice = int(input("Выбирете пункт: \n1.По заданию с малыми числами\n2.Выйти из программы\n"))
    if choice == 1:
        msg = str(input("\nВведите текст: "))
        p = rand_prime()
        g = random.randint(2, p)
        choice = int(input("Ввыбрать закрытый ключ\n1.Вручную\n2.Рандом\n"))
        if choice == 1:
            x = int(input("750< "))
        elif choice == 2:
            x = random.randint(750, p - 1)
        else:
            print("не верный выбор")
        y = pow(g, x, p)
        k = rand_primeK()
        print("p= ", p, " g= ", g, " y= ", y, " k= ", k)
        print("р- ", CheckIfProbablyPrime(p))
        print("к- ", CheckIfProbablyPrime(k))
        ct, a = encryption(msg, p, y, g)
        print("Оригинальный текст: ", msg, "\nЗашифрованый текст: ", ct)
        print("Расшифрованый текст: ", "".join(decryption(ct, a, x, p)))
        continue

    else:
        break
