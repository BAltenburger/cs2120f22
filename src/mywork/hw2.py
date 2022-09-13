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
    
    s.reset()
    # 2. X, Y ⊢ X ∧ Y      
    # As propostion in PL: X /\ Y --> X /\ Y
    C2 = Implies(And(X,Y), (And(X,Y)))
    s.add(Not(C2))
    # I believe it's valid
    print_result(s,2)
    
    s.reset()
    #3. X ∧ Y ⊢ X
    # As propostion in PL: X /\ Y --> X
    C3 = Implies(And(X,Y), X)
    s.add(Not(C3))
    # I believe it is valid
    print_result(s,3)
    
    s.reset()
    # 4. X ∧ Y ⊢ Y
    # As proposition in PL: X /\ Y --> Y
    C4 = Implies(And(X,Y), Y)
    s.add(Not(C4))
    # I believe it is valid
    print_result(s, 4)
    
    s.reset()
    # 5. ¬¬X ⊢ X             
    # As propostion in PL: ~~X --> X
    C5 = Implies(Not(Not(X)), X)
    # I believe it is valid
    s.add(Not(C5))
    print_result(s, 5)
    
    s.reset()
    #6. ¬(X ∧ ¬X)  
    # As proposition in PL: ~(X /\ ~X)
    C6 = Not(And(X, Not(X)))
    # I believe it is valid
    s.add(Not(C6))
    print_result(s,6)
    
    s.reset()
    # 7. X ⊢ X ∨ Y
    # As propostion in PL: X --> X \/ Y
    C7 = Implies(X, Or(X,Y))
    # I believe this is valid
    s.add(Not(C7))
    print_result(s,7)

    s.reset()
    # 8. Y ⊢ X ∨ Y  
    # As proposition in PL: Y --> X \/ Y
    C8 = Implies(Y, Or(X,Y))
    # I believe this is valid
    s.add(Not(C8))
    print_result(s, 8)
    
    s.reset()
    # 9. X → Y, ¬X ⊢ ¬ Y   
    # As proposition in PL: (X --> Y) /\ (~X --> ~Y)
    C9 = And(Implies(X,Y), Implies(Not(X), Not(Y)))
    # I believe this is not valid
    s.add(Not(C9))
    print_result(s, 9)   
    
    s.reset()
    # 10. X → Y, Y → X ⊢ X ↔ Y  
    # As propostion in PL: X--> y /\ Y --> X --> X <-->Y

    



    




def print_result(s, question_number):
    if (s.check() == unsat):
        print("C" + str(question_number)+ " is valid.")
    else:
        print("C" + str(question_number) + " is not valid. Here is a counter-example: ", s.model())
hw2()