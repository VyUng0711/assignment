def foo_or(a,b):
    #returns a or b
    return a or b

def foo_and(a,b):
    #returns a and b
    return a and b

def id1(a,b):
    #returns a
    return a

def id2(a,b):
    #returns b
    return b
    
def not_id1(a,b):
    #return not a 
    return not a
    
def not_id2(a,b):
    #return not b
    return not b

def implication(a,b):
    #returns a->b
    return (not a) or b
    
def a_or_notb(a,b):
    #returns a or not b
    return a or (not b)

def nota_or_notb(a,b):
    #returns b ->-a
    return not a or not b


#Inputs: premises into f and g, conclusion into h; inputs should take the form of function
def valid(f,g,h):
#There are two values True and False that we assign on a and b
    values = [True, False]
#At the beginning, we assign variable test as EMPLY
    test = ""
#For loop: for loop goes through all the possibilities that the combination of values of a and b could be
#Then it will loop at least one time and at most four times because we have four combinations, and a break
    for a in values:
        for b in values:
#Each time it wil test the conclusion first 
#If the conclusion is True, this this line still keeps the argument valid no matter what the two premises are
            if h(a,b) == True:
#Then we assign test as TRUE
                test = "True"
#If the conclusion is False, continue to check the two premises
            else:
#If the two premises are both True while the conclusion is false, this line makes the argument invalid
                if f(a,b) == True and g(a,b) == True:
#Then we assign test as FALSE and break the loop 
                    test = "False"
                    break
#The other cases: the argument is still valid
                else:
                    test = "True"
#This function return test
    return test
    

#Testing with modus ponens
print valid(implication, id1, id2)
#Testing with modus tollens
print valid(implication, not_id2, not_id1)
#Testing with disjunctive syllogism
print valid(foo_or, not_id1, id2)
#Testing with (A and B) -> (-A or B), B -> -A, conclusion: A or -B
print valid(implication(foo_and,implication), nota_or_notb, a_or_notb)
#Testing premises: A or B, B, conclusion: A
print valid(foo_or, id2, id1)
# tests premises: A or (A and B), B, conclusion: A
print valid(foo_or(id1,foo_and), id2, id1)
