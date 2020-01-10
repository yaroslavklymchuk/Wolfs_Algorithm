from datetime import datetime
from heroes import Human, Rabbit, Tree, Cabbage
import random
import itertools
import numpy as np


class Evolution:
    def __init__(self, max_iterations):
        self.__max_iterations = max_iterations

    creatures_symbols_mapping = {'H': Human,
                                 'R': Rabbit,
                                 'T': Tree,
                                 'C': Cabbage
                                 }

    def _create_evolution_matrix(self, shape, probability=0.5, random_seed=42):
        x_shape, y_shape = shape
        evo_matrix = np.zeros(shape)
        random.seed(random_seed)
        for i, j in itertools.product(range(x_shape), range(y_shape)):
            if np.random.uniform(0, 1, 1) > probability:
                evo_matrix[i][j] = random.choice(list(self.creatures_symbols_mapping.keys()))

        return evo_matrix


