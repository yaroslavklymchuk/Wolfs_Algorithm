from heroes import Human, Rabbit, Tree, Cabbage, Wolf
import random
import itertools
import numpy as np


class Evolution:
    def __init__(self, max_iterations):
        self.__max_iterations = max_iterations

    creatures_symbols_list = ['H', 'R', 'W', 'C', 'T']
    creatures_list = [Human(0, 0, 0), Rabbit(0, 0, 0), Wolf(0, 0, 0), Cabbage(0), Tree(0)]
    creatures_mapping = dict(zip(creatures_symbols_list, creatures_list))

    def _create_evolution_matrix(self, shape, probability=0.5, random_seed=42):
        x_shape, y_shape = shape
        evo_matrix = np.zeros(shape).astype(object)
        random.seed(random_seed)
        for i, j in itertools.product(range(x_shape), range(y_shape)):
            if np.random.uniform(0, 1, 1) > probability:
                evo_matrix[i][j] = random.choice(self.creatures_list)

        return evo_matrix

    @staticmethod
    def rotate_heros(hero1, hero2):
        if hero1.symbol == 'H' and hero2.symbol == 'W':
            hero1.can_identify_evil = 1
            return hero2
        elif hero1.symbol == 'R' and hero2.symbol == 'W':
            hero1.can_identify_evil = 1
            return hero2
        elif hero1.symbol == 'R' and hero2.symbol == 'C':
            return hero1
        elif hero1.symbol == 'H' and hero2.symbol == 'T':
            return hero1
        elif hero1.symbol == 'W' and hero2.symbol == 'T':
            return hero2
        elif hero1.symbol == 'R' and hero2.symbol == 'T':
            return hero2
        else:
            return None

    def _evolute(self, evolution_matrix):
        for i, j in itertools.product(range(evolution_matrix.shape[0]), range(evolution_matrix.shape[1])):
            if evolution_matrix[i][j]:
                creature = evolution_matrix[i][j]
                children = creature.make_child()
                creature.age += 1
                if creature.age > creature.max_age:
                    evolution_matrix[i][j] = 0
                if children:
                    for k in range(len(children)):
                        for i1, j1 in itertools.product(range(evolution_matrix.shape[0]), 
                                                        range(evolution_matrix.shape[1])):
                            if not evolution_matrix[i1][j1]:
                                evolution_matrix[i1][j1] = children[k]
                            else:
                                new_hero = self.rotate_heros(children[k], evolution_matrix[i1][j1])
                                if new_hero:
                                    evolution_matrix[i1][j1] = new_hero
        return evolution_matrix

    def main(self, evolution_matrix_init):
        new_evo_matrix = evolution_matrix_init
        for iteration in range(self.__max_iterations):
            new_evo_matrix = self._evolute(new_evo_matrix)
            ravel_matrix = new_evo_matrix.flatten().tolist()
            creatures_mapping = {}
            for creature in self.creatures_symbols_list:
                creatures_mapping[creature] = len(list(filter(lambda x: x.symbol.upper() == creature,
                                                              [el for el in ravel_matrix 
                                                               if not isinstance(el, int)])))
            print('Iteration: {}, qty Humans: {}, qty Rabbits: {}, qty Wolfs: {}, '
                  'qty Cabbages: {}, qty Trees: {}'.format(iteration, creatures_mapping.get('H'),
                                                           creatures_mapping.get('R'), creatures_mapping.get('W'),
                                                           creatures_mapping.get('C'), creatures_mapping.get('T')))
        return new_evo_matrix