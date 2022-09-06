from z3 import *

def sqrt(n) :
    sqrtn = Real('sqrtn')
    s = Solver()
    s.add(sqrtn*sqrtn==n) # replace True with required declarative spec
    s.add(sqrtn >= 0)
    # the rules it needs to follow, so both must be true for it all to be true
    isSat = s.check()
    if (isSat == sat) :
        return s.model()
    return -1
    
print(sqrt(16))