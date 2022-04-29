"""Zoe Houde & Ethan Meyer
Final Project INST326"""

"""This is the hardoced version of the outline. We need to get the array saved so its not hardcoded in by using self. methods
I was was also going to add a more complex imput for meal, amount just stood as a place holder"""
import re
class Fraternity:
    def __init__(self, frat):
        self.frat = frat
        entree = input("Entree?")
        sides = input("sides?")
        packaged = input("pack?")
        servings = input("How many servings do you have leftover?:")
        allergens = input("Does this food have potential allergens?:")
        order = [entree, sides, packaged, servings, allergens]
        finished = [frat, order]
        print(finished)

class Sorority:
    def __init__(self, sor):
        self.sor = sor
        entree = input("Entree?")
        sides = input("sides?") 
        packaged = input("pack?")
        servings = input("How many servings do you have leftover?:")
        allergens = input("Does this food have potential allergens?:")
        order = [entree, sides, packaged, servings, allergens]
        finished = [sor, order]
        print(finished)
       

#acting as main. should be a loop for each time a new input is created, a new frat or soriority
#regex functions limit user input to avoid errors in address, food input, name input, etc.

frats_dict = {}
sor_dict = {}
print("welcome")
x = input("To begin, please state if you represent either a Fraternity or Sorority?:")
if x =="Fraternity":
    print("To begin, please enter your greek letters, if you are not in our system, we will add you:")
    Fname = input("Greek Letters: ")
    if Fname not in frats_dict:
        print("It appears you are not in our database, please enter your address like '123 Rocky Road'")
        Faddy = input()
        frats_dict.update({Fname:Faddy})
        Fraternity(Fname)
        exit()       
    
elif x =="Sorority":
    print("To begin, please enter your greek letters, if you are not in our system, we will add you:")
    Sname = input("Greek Letters: ")
    if Sname not in sor_dict:
        print("It appears you are not in our database, please enter your address like '123 Rocky Road'")
        Saddy = input()
        frats_dict.update({Sname:Saddy})
        Sorority(Sname)
        exit()
        
  
else:
    print("please try again")







    



