class Creature:
    def __init__(self, age, has_child_this_year, can_identify_evil, symbol, max_age):
        self.age = age
        self.has_child_this_year = has_child_this_year
        self.can_identify_evil = can_identify_evil
        self.symbol = symbol
        self.max_age = max_age

    def make_child(self, lower_age, upper_age, max_qty_child):
        if lower_age <= self.age <= upper_age and not self.has_child_this_year:
            self.has_child_this_year = True
            return [Creature(0, 0, 0, 'A', 0)] * max_qty_child


class Human(Creature):
    def __init__(self, age, has_child_this_year, can_identify_evil, symbol='H', max_age=70):
        super().__init__(age, has_child_this_year, can_identify_evil, symbol, max_age)

    def make_child(self, lower_age=20, upper_age=35, max_qty_child=2):
        if lower_age <= self.age <= upper_age and not self.has_child_this_year:
            self.has_child_this_year = True
            return [Human(0, 0, 0)] * max_qty_child


class Wolf(Creature):
    def __init__(self, age, has_child_this_year, can_identify_evil=0, symbol='W', max_age=10):
        super().__init__(age, has_child_this_year, can_identify_evil, symbol, max_age)

    def make_child(self, lower_age=2, upper_age=8, max_qty_child=6):
        if lower_age <= self.age <= upper_age and not self.has_child_this_year:
            self.has_child_this_year = True
            return [Wolf(0, 0, 0)] * max_qty_child


class Rabbit(Creature):
    def __init__(self, age, has_child_this_year, can_identify_evil, symbol='R', max_age=6):
        super().__init__(age, has_child_this_year, can_identify_evil, symbol, max_age)

    def make_child(self, lower_age=2, upper_age=5, max_qty_child=8):
        if lower_age <= self.age <= upper_age and not self.has_child_this_year:
            self.has_child_this_year = True
            return [Rabbit(0, 0, 0)] * max_qty_child


class Cabbage:
    def __init__(self, age, symbol='C', max_age=2):
        self.age = age
        self.symbol = symbol
        self.max_age = max_age

    def make_child(self, max_qty_child=20):
        if self.age >= 2:
            return [Cabbage(0)] * max_qty_child


class Tree:
    def __init__(self, age, symbol='T', max_age=100):
        self.age = age
        self.symbol = symbol
        self.max_age = max_age

    def make_child(self, max_qty_child=5):
        if self.age >= 5:
            return [Tree(0)] * max_qty_child