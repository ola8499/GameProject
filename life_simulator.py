
class Human(object):
    def __init__(self, hunger, trusty, energy):
        self.hunger = hunger
        self.trusty = trusty
        self.energy = energy

    def __wasting(self):
        self.hunger -= 1
        self.trusty -= 1
        self.energy -= 1

    def eating(self):
        answer = None
        while not answer:
            question = "What do you what to eat? (breakfast / dinner / supper) "
            answer = input(question).lower()
            if answer == "breakfast":
                self.hunger += 10
            elif answer == "dinner":
                self.hunger += 15
            elif answer == "supper":
                self.hunger += 5
            else:
                answer = None

    def drinking(self):
        answer = None
        while not answer:
            question = "What do you what to drink? (juice / water / coffee) "
            answer = input(question).lower()
            if answer == "breakfast":
                self.hunger += 10
            elif answer == "dinner":
                self.hunger += 15
            elif answer == "supper":
                self.hunger += 5
            else:
                answer = None
    def sleeping(self):

class Baby(Human):
    def __init__(self, hunger, trusty, energy, boredom):
        super(Baby,self).__init__(hunger, trusty, energy)
        self.boredom = boredom

    def playing(self):

    def crying(self):

    def begging(self):

class Parent(Human):
    def __init__(self, hunger, trusty, energy, money, boredom):
        super(Parent, self).__init__(hunger, trusty, energy)
        self.money = money
        self.boredom = boredom

    def play_with_kids(self):

    def feed_child(self):

    def working(self):
