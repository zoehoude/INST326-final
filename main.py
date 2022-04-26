"""Zoe Houde & Ethan Meyer
Final Project INST326"""

"""This is the hardoced version of the outline. We need to get the array saved so its not hardcoded in by using self. methods
I was was also going to add a more complex imput for meal, amount just stood as a place holder"""
class Fraternity:
    def __init__(self, frat):
        self.frat = frat
        entree = input("Entree?")
        sides = input("sides?")
        packaged = input("pack?")
        order = [entree, sides, packaged]
        finished = [frat, order]
        print(finished)

class Sorority:
    def __init__(self, sor):
        self.sor = sor
        entree = input("Entree?")
        sides = input("sides?")
        packaged = input("pack?")
        order = [entree, sides, packaged]
        finished = [sor, order]
        print(finished)
       

#acting as main. should be a loop for each time a new input is created, a new frat or sorioert
print("welcome")
x = input("Frat or Sor?:")
if x == "Frat":
    Fname = input("Greek Letters: ")
    Flocation = input("Street Address as '123 Rocky Road': ")
    frat = [Fname, Flocation]
    Fraternity(frat)
    exit()
    
if x == "Sor":
    Sname = input("Greek Letters: ")
    Slocation = input("Street Address as '123 Rocky Road': ")
    sor = [Sname, Slocation]
    Sorority(sor)
    exit()
    
    





def add_order(frats): 
    choice = input("Submit an order?(yes or no)")
    if choice =="no":
        x = print("Ok, returning you back to home")
        return x
        
    


