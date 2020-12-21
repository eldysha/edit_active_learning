import pandas as pd
import ast

import sklearn

from regression import *
import pickle
import random

# FZ AUSILIARIA
def mul_x(list_coeff, list_scores, x):
    for scores in list_scores:
        i = 0
        while i < x:
            scores[i] = scores[i] * list_coeff[i]
            i += 1
    return list_scores