'''
Let's talk about "Scope" in Python
Scope basically means the place where that code reachs
It exists "Local Scope" and "Global Scope"
'''

x = 1 #This variable is on the "primary" scope

def primary():
    x = 2 #Now this "x" has nothing to do with the previous "x" that we defined
    
    def secondary():
        x = 3 #The same for this one
        print(x)

    secondary()
    print(x)

primary()
print(x)

#But there is something, if i do not define another "x" variable in the function scope
#The "x" that was already defined, reachs the scope of the function
#Is like if the previous scope is the most important, and reachs all the others