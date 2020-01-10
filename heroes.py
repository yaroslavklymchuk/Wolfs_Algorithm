class Creature:
    def __init__(self, age, has_child_this_year, can_identify_evil):
        self.__age = age
        self.__has_child_this_year = has_child_this_year
        self.can_identify_evil = can_identify_evil

    def _make_child(self, lower_age, upper_age, max_qty_child):
        if lower_age <= self.__age <= upper_age and not self.__has_child_this_year:
            return [Creature(0, 0, 0)] * max_qty_child


class Human(Creature):
    def __init__(self, age, has_child_this_year, can_identify_evil):
        super().__init__(age, has_child_this_year, can_identify_evil)

    def _make_child(self, lower_age=20, upper_age=35, max_qty_child=2):
        if lower_age <= self.__age <= upper_age and not self.__has_child_this_year:
            return [Human(0, 0, 0)] * max_qty_child


class Wolf(Creature):
    def __init__(self, age, has_child_this_year, can_identify_evil=0):
        super().__init__(age, has_child_this_year, can_identify_evil)

    def _make_child(self, lower_age=2, upper_age=8, max_qty_child=6):
        if lower_age <= self.__age <= upper_age and not self.__has_child_this_year:
            return [Wolf(0, 0, 0)] * max_qty_child


class Rabbit(Creature):
    def __init__(self, age, has_child_this_year, can_identify_evil):
        super().__init__(age, has_child_this_year, can_identify_evil)

    def _make_child(self, lower_age=2, upper_age=5, max_qty_child=8):
        if lower_age <= self.__age <= upper_age and not self.__has_child_this_year:
            return [Rabbit(0, 0, 0)] * max_qty_child


class Cabbage:
    def __init__(self, age):
        self.__age = age

    def _make_child(self, max_qty_child=20):
        if self.__age >= 2:
            return [Cabbage(0)] * max_qty_child


class Tree:
    def __init__(self, age):
        self.__age = age

    def _make_child(self, max_qty_child=5):
        if self.__age >= 5:
            return [Tree(0)] * max_qty_child







