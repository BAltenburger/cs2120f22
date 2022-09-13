# Be sure you've done pip install z3-solver
from telnetlib import X3PAD
from z3 import *


# Here's a file you can often copy as a starting 
# point on a working program to solve some problem
# of interest. Here the problem is to compute and
# return a non-negative square root of argument, n 
def hw2():
    
    
    # Create z3 variable(s) representing the unknown
    # Here, the unknown, x, is the square root of n.
    X, Y, Z = Bools('X Y Z')
    s = Solver()
    # 1. X ∨ Y, X ⊢ ¬Y 
    # As proposition in PL: ((X \/ Y) /\ X) -> ~Y
    C1 = Implies(And(Or(X,Y),X),Not(Y))
    s.add(Not(C1))
    # I believe it's not valid
    print_result(s, 1)
    
    # 2, 

def print_result(s, question_number):
    if (s.check() == unsat):
        print("C" + str(question_number)+ " is valid.")
    else:
        print("C" + str(question_number) + " is not valid. Here is a counter-example: ", s.model())
hw2()