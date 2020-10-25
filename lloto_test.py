from random import randint


def rand_excl(excl):
    outInt = 0
    while outInt == 0:
        rand = randint(1, 90)
        if rand not in excl:
            outInt = rand
    return outInt


class Card:
    def __init__(self, name):
        self.name = name
        self.numbers = []
        self.line1 = []
        self.line2 = []
        self.line3 = []
        for i in range(1, 16):
            num = rand_excl(self.numbers)
            self.numbers.append(num)
        self.numbers = sorted(self.numbers)
        for i in self.numbers:
            countLine1 = sum(map(lambda x: x > 0, self.line1))
            countLine2 = sum(map(lambda x: x > 0, self.line2))
            countLine3 = sum(map(lambda x: x > 0, self.line3))
            addEmpty = randint(1, 2)
            if len(self.line1) < 8 and countLine1 < 5:
                self.line1.append(i)
            else:
                if len(self.line2) < 8 and countLine2 < 5:
                    self.line2.append(i)
                else:
                    if len(self.line3) < 8 and countLine3 < 5:
                        self.line3.append(i)
            if len(self.line1) < 7:
                if addEmpty == 2 and countLine1 <= 5:
                    self.line1.append(0)
            else:
                if len(self.line2) < 7:
                    if addEmpty == 2 and countLine2 <= 5:
                        self.line2.append(0)
                else:
                    if len(self.line3) < 7:
                        if addEmpty == 2 and countLine3 <= 5:
                            self.line3.append(0)

    def __str__(self):
        print(self.name, '\n---------------------------')
        for i in self.line1:
            print(' ' if i == 0 else (i if (i in self.numbers) else '-'), ' ', end='')
        print(' ')
        for i in self.line2:
            print(' ' if i == 0 else (i if (i in self.numbers) else '-'), ' ', end='')
        print(' ')
        for i in self.line3:
            print(' ' if i == 0 else (i if (i in self.numbers) else '-'), ' ', end='')
        print(' ')
        print('---------------------------')
        return ''

    def checkNumber(self, number):
        return number in self.numbers

    def deleteNumber(self, number):
        if number in self.numbers:
            self.numbers.remove(number)

    def isEmpty(self):
        return len(self.numbers) == 0


class Keg:
    def __init__(self):
        self.numbers = []

    def getKeg(self):
        kegNumber = rand_excl(self.numbers)
        self.numbers.append(kegNumber)
        return kegNumber

    def isEmpty(self):
        return len(self.numbers) == 90


humanCard = Card('Игрок')
computerCard = Card('Компьютер')
keg = Keg()
endGame = False
while not endGame:
    print(computerCard)
    print(humanCard)
    newKeg = keg.getKeg()
    print('Текущий номер бочонка: ', newKeg)
    inStr = input('Есть цифра (y/n)')
    if inStr == 'y':
        if humanCard.checkNumber(newKeg):
            humanCard.deleteNumber(newKeg)
        else:
            endGame = True
    elif inStr == 'n':
        if humanCard.checkNumber(newKeg):
            endGame = True
    elif computerCard.checkNumber(newKeg):
        computerCard.deleteNumber(newKeg)
    elif keg.isEmpty() or humanCard.isEmpty() or computerCard.isEmpty():
        endGame = True
print('Конец игры')
if computerCard.isEmpty():
    print('Компьютер победил!')
if humanCard.isEmpty():
    print('Игрок победил!')
if not computerCard.isEmpty() and not humanCard.isEmpty():
    print('Вы ошиблись и проиграли!')