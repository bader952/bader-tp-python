def exo1():
    for i in range (0, 500) :
        print ("je dois faire des sauvegardes reguliere de mes fichier")

exo1()


def exo2():
    pair = []
    for a in range(0, 1000, 2):
        pair.append(a)
    print(pair)
    impair = {n + 1 for n in pair}
    print(impair)

exo2()

def exo3():
    for b in range(0, 10):
        print(b, "*", 13, "=", b * 13)


exo3()

def exo4():
    m = input("enter a word : ")
    print(len(m))

exo4()


def exo5():
    e = int(input("enter a number : "))

    if (e % 2)== 0:
        print("{0}) est pair".format(e))
    else:
        print("{0} est impair" .format(e))

exo5()


def exo6():
    nbr = int(input("nombre entre 10 et 20"))
    while(nbr < 10 or nbr > 20):
        if nbr < 10:
            print("Plus grand !")
        elif nbr > 20:
            print("Plus petit !")
        nbr = int(input("nombre entre 10 et 20"))
    print("cool")

exo6()


def exo7():
    nbr = int(input("Donne moi un nombre"))
    for i in range(10):
        nbr = nbr + 1
        print(nbr)


exo7()


def exo8():
    nbr = int(input("Donne moi un nombre"))
    i = 0
    for i in range(10):
        i = i + 1
        somme = nbr * i
        print(nbr, "*", i, "=", somme)

exo8()


def exo9():
    nbr = int(input("Donne moi un nombre"))
    count = 0
    for i in range(nbr + 1):
        count = i + count
    print(count)

exo9()

def exo10():
    nbr = int(input("Quel est ton âge?"))
    if nbr == 6 or nbr == 7:
        print("Poussin")
    elif nbr == 8 or nbr == 9:
        print("Pupille")
    elif nbr == 10 or nbr == 11:
        print("Minime")
    elif nbr >= 12:
        print("Cadet")
    else:
        print("too small")

exo10()


def exo11():
    nbr = int(input("Nombre d'articles ?"))
    euro = int(input("prix unitaire?"))
    prixht = nbr*euro
    tva = prixht * 1.20
    print("nombres d'articles :", nbr)
    print("prix HT :", prixht)
    print("Prix TTC :", tva)

exo11()


