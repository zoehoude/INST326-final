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
        pick_up = input("What time can we pick up? (530-630, 630-730, 730-830):"
        order = [entree, sides, packaged, servings, allergens]
        finished = [frat, order, pick_up]
        print(finished)

class Sorority:
    def __init__(self, sor):
        self.sor = sor
        entree = input("Entree?")
        sides = input("sides?") 
        packaged = input("pack?")
        servings = input("How many servings do you have leftover?:")
        allergens = input("Does this food have potential allergens?:")
        pick_up = input("What time can we pick up? (530-630, 630-730, 730-830):"
        order = [entree, sides, packaged, servings, allergens]
        finished = [sor, order, pick_up]
        print(finished)
        
        
class preg_aid_center:
    def __init__(self, pac):
        bank_name_pac = "Pregnancy Aid Center INC - Food Distribution Center"
        address = "4809 Greenbelt Rd, College Park, MD 20740"
        pref_pick_up_time = {6,7} #tuple for pick up times 6-7
        phone = "3014119150"
        pac_info = [bank_name_pac, phone, pref_pick_up_time]
 
        
class takoma_park_food:
    def __init__(self, takoma):
        bank_name_takoma = "Takoma Park Food Pantry"
        address = "7001 New Hampshire Ave, Takoma Park, MD 20912"
        pref_pick_up_time = {530,630} 
        phone = "2404502092" #is there a way we can hyper link this so when it prints on the screen thte app can just click 
        takoma_info = [bank_name_takoma,  phone, pref_pick_up_time]
        
        
class umd_food:
    def __init__(self, umd):
        bank_name_umd = "UMD Campus Pantry"
        address = "South Campus Dining Hall, 7093 Preinkert Dr, College Park, MD 20740"
        pref_pick_up_time = {730,830} 
        phone = "3014059579"
        umd_info = [bank_name_umd,  phone, pref_pick_up_time]
        
       

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


#comparing pickup times from soroiry/frat input to the times the food banks selectted previously

if pick_up == pref_pick_up_time:
    print(umd_info)
                        
else:
    print("Try again")
    



