import numpy

class slot_rack:
    def __init__(self):
        self.capacity=0

    def deposit(self, deposit):
        self.capacity+=deposit

    def jogar(self, spent):

        if self.capacity<spent:
            return 2

        self.capacity-=spent

        symbols = ["ate","mamma", "banger", "pussy", "serve", "cunt", "slay"]
        winning = [5, 10, 20, 70, 200, 1000, 100000]

        first = numpy.random.choice(numpy.arange(1, 8), p=[50/156, 40/156, 30/156, 20/156, 10/156, 5/156, 1/156])
        second = numpy.random.choice(numpy.arange(1, 8), p=[50/156, 40/156, 30/156, 20/156, 10/156, 5/156, 1/156])
        third = numpy.random.choice(numpy.arange(1, 8), p=[50/156, 40/156, 30/156, 20/156, 10/156, 5/156, 1/156])

        if first==second==third:
            self.capacity+=winning[first-1]

        print(" First symbol: ", symbols[first], "\n Second symbol: ", symbols[second], "\n Third symbol: ", symbols[third])

        if self.capacity==0:
            return 0
        else:
            return 1    

def slay():
    cont= True
    game = slot_rack()
    deposit = int(input(" Hey, welcome to Slot Rack, the Cunt SLayer 9000 machine, please enter how much you want to deposit: "))    
    game.deposit(deposit)
    while cont:
        spend = int(input(" How much do you want to bet? "))
        yes=game.jogar(spend)

        while yes==2:
            spend = int(input(" Sorry, that's not valid. How much do you want to bet? "))
            yes=game.jogar(spend)

        if yes==0:
            cont=False

        else:
            win= input(" Do you want to continue playing? Y/N: ")
            while win not in ["Y","N"]:
                win = input(" Sorry I didn't get that. Do you want to continue playing? Y/N: ")
            if win=="Y" or win=="y" or win=="yes":
                cont=True
            elif win == "N" or win=="n" or win=="no":
                cont=False            

    print(" Thank you for playing! Come back to Slot Rack anytime!") 

slay()                