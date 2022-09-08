# Be sure you've done pip install z3-solver
from z3 import *


# Here's a file you can often copy as a starting 
# point on a working program to solve some problem
# of interest. Here the problem is to compute and
# return a non-negative square root of argument, n 
def homework_two():
    
    
    # Create z3 variable(s) representing the unknown
    # Here, the unknown, x, is the square root of n.
    X,Y,Z = Bools('X Y Z')
    
    
    # Important: This is where you express what
    # values count as solutions using propositional
    # logic, but in the slightly different syntax
    # of Z3 expressions.
    s = Solver()
    
    # 1. X ∨ Y, X ⊢ ¬Y             -- affirming the disjunct

    C1 = Implies(And(Or(X,Y),X), Not(Y))
    s.add(Not(C1))
    
    
    # Create a Z3 "SMT" solver object, and give it 
    # the overall constraint to be solved, here C.
    
    
    
    # Run the Z3 model finder, capturing "sat"
    # or "unsat" as the return value 
    isSat = s.check()
    
    # If there's a model/solution return it 
    if (isSat == unsat):
        print("It is valid")
    # otherwise return inconsistent value for error
    else:
            print("Here is a counter example: " + str(s.model()))

# Set up and run the function and report its results
s = homework_two()

