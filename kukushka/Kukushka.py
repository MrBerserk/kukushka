from random import randint


def kukushka(name):

    # name = 'Dimasik '
    years = randint(1, 15)

    if years >= 5:
        return name + ', Вам осталось жить ' + str(years) + ' лет'

    if years == 1:
        return name + ", Вам осталось жить " + str(years) + " год"

    else:
        return name + ', Вам осталось жить ' + str(years) + ' года'




