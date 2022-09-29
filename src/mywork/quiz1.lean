/-
Betsy Altenburger
hjc6uh


CS2120 Fall 2022 Sullivan. Quiz #1. Edit your answers into
this file using VSCode. Save the file to your *local* hard 
drive (File > Save As > local > ...). Submit it to the Quiz1
assignment on Collab.
-/

/-
#1: For each of the following questions give a yes/no answer 
and then a very brief explanation why that answer is correct.
To explain why your answer is correct, name the specific rule
of inference that tells you it's correct, or explain that 
there is no such valid inference rule.
-/

/-
#1A

If a ball, b, is round *and* b is also red, is b red?

A: yes/no: Yes

B: Why? 
We know this to be true because of the defintion of and.
If b is round and red, then it must be red. For an and
statment to be true, both of the conditions must be true.
This uses the and elimination rule.


#1B

If flowers make you happy and chocolates make you happy,
and I give you flowers *or* I give you chocolates, will
you be happy?

A: yes/no:  Yes

B: Why?
Assuming since there is no * around the and, the person is happy
to recieve either flowers or chocolates meaning they don't nesciarly need both to be happy.
From that assumption, if they are given flowers or chocolate they will be happy.
This is because if flower → happy and chocolates → happy, then flowers ∨ chocolates → happy.
This is the or elimination rule.

#1C: If giraffes are just zebras in disguise, then the 
moon is made of green cheese?

A. yes/: Yes

B. Why?
Giraffes are not just zebras in diguise. This is false, and from false anything is true.
Looking at the logic table for implies shows this, and the false elimination rule also proves this.

#1D. If x = y implies that 0 = 1, then is it true that
x ≠ y?

A. yes/no: yes

B. Why? 
If x = y means that 0 = 1, the premise is false. From false anything can follow, so it is true that x does not 
equal y. This is the false elmination rule.


#1E. If every zebra has stripes and Zoe is a Zebra then
Zoe has stripes.

A. yes/no: Yes

B. Why?
If we assume the premise to be true, that is for all zerbras, they have stripes and Zoe is a zebra.
Then it follows that zoe is a zebra.
This uses the for all elmination rule.

#1F. If Z could be *any* Zebra and Z has stripes, then 
*every* Zebra has stripes.

A. Yes/no: No

B: Why?
No such inference rule exists saying that any equals every. This is like saying
for all is logically the same as there exists. This is incorrect logic.


#1G. If whenever the wind blows, the leaves move, and 
the leaves are moving, then the wind is blowing.

A. yes/no: yes

B. Why? 
If wind → leaves moving and leaves moving → wind is the statement, then this can be prove
with the iff introduction rule. Becuase X implies Y and Y implies X, it works both ways.
This does work because it can be read as an if and only if statment. 


#1H: If Gina is nice *or* Gina is tall, and Gina is nice,
then Gina is not tall. (The "or" here is understood to be
the or of predicate logic.)

A. yes/no: no

B. Why?
The or elimination rule does not work this way. Assuming that Gina is nice does not mean that 
she is not tall. The or elmination rule does not work for proving something to be false.

-/



/- 
#2

Consider the following formula/proposition in propositional
logic: X ∨ ¬Y.

#2A: Is is satisfiable? If so, give a model (a binding of 
the variables to values that makes the expressions true).

Yes, this is satisfiable because there exists an interpretation that makes this true.
One mode would be X = True and Y = False

#2B: Is it valid? Explain your answer. 
No, this is not valid. It is not true under all interpretations. 
One model where this evaluates to false is X = False and Y = True.
false ∨ ¬ true = false ∨ false = false 

-/


/-
#3: 

Express the following propositions in predicate logic, by
filling in the blank after the #check command.

If P and Q are arbitrary (any) propositions, then if (P is 
true if and only if Q is true) then if P is true then Q is 
true.
-/
#check ∀ (P Q: Prop), P ↔ Q → P → Q 

/-
Note: Since it said P and Q could be any propositions, I assumed this meant for all.
However, the statement above would also work with a there exists key as well. 
-/


/-
#4 Translate the following expressions into English.
The #check commands are just Lean commands and can
be ignored here. 
-/


-- A
#check ∀ (n m : ℕ), n < m → m - n > 0

/-
Answer: 
For all natural numbers, n and m, if n is greater than m,
then m-n is greater than zero meaning m-n is a postive number.

-/

-- B

#check ∃ (n : ℕ), ∀ (m : nat), m >= n

/-
Answer: There exists some natural number n that for all natural numbers, m, 
m is greater than or equal to n.
-/


-- C

variables (isEven: ℕ → Prop) (isOdd: ℕ → Prop)
#check ∀ (n : ℕ), isEven n ∨ isOdd n

/-
Answer:
For all natural numbers, n, n is even or is odd.
-/


-- D

#check ∀ (P : Prop), P ∨ ¬P

/-
Answer:
For all propositions p, p or not p will always evaluate to true.
-/


-- E

#check ∀ (P : Prop), ¬(P ∧ ¬P)

/-
Answer:
For all propositions p, the negation of p or not but will also always be true.
-/


/-
#5 Extra Credit

Next we define contagion as a proof of a slightly long
proposition. Everything before the comma introduces new
terms, which are then used after the comma to state the
main content of the proposition. 

Using the names we've given to the variables to infer
real-world meanings, state what the logic means in plain
natural English. Please don't just give a verbatim reading
of the formal logic. 
-/

variable contagion : 
  ∀ (Animal : Type) 
  (hasVirus : Animal → Prop) 
  (a1 a2 : Animal) 
  (hasVirus : Animal → Prop)
  (closeContact : Animal → Animal → Prop), 
  hasVirus a1 → closeContact a1 a2 → hasVirus a2

/- 
For all animals, if one animal has the virus and was in close contact with another animal, 
then if follow that the second animal has the virus. 
-/