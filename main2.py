"""Zoe Houde & Ethan Meyer
Final Project INST326"""

import re

class Greek:
    def __intit__(self):
        self.greek = greek
        entree = input("Entree?")
        sides = input("sides?")
        packaged = input("pack?")
        servings = input("How many servings do you have leftover?:")
        allergens = input("Does this food have potential allergens?:")
        pick_up = input("What time can we pick up? (530-630, 630-730, 730-830:")
        order = [entree, sides, packaged, servings, allergens]
        finished = [frat, order, pick_up]
        print(finished)


class Fraternity(Greek):
    '''initializing functions, variables, getting user input, combining inputs into lists for frats'''
    def __init__(self, frat):
        self.frat = frat
    def calc_f(self,frat):
        frat_inh = Greek.identify()
        frat_start = frat_inh.print("Fraternity mode")

class Sorority(Greek):
    def __init__(self, sor):
        '''initializing functions, variables, getting user input, combining inputs into lists for sororities'''
        self.sor = sor
    def calc_s(self):
        return Greek.identify()
        
        
class preg_aid_center:
    def __init__(self, pac):
        '''initializing functions, variables,getting user input, combining inputs into lists for pac'''
        bank_name_pac = "Pregnancy Aid Center INC - Food Distribution Center"
        address = "4809 Greenbelt Rd, College Park, MD 20740"
        pref_pick_up_time_pac = {6,7} #tuple for pick up times 6-7
        phone = "3014119150"
        pac_info = [bank_name_pac, phone, pref_pick_up_time]
 
        
class takoma_park_food:
    def __init__(self, takoma):
        '''initializing functions, variables,getting user input, combining inputs into lists for takoma'''
        bank_name_takoma = "Takoma Park Food Pantry"
        address = "7001 New Hampshire Ave, Takoma Park, MD 20912"
        pref_pick_up_time_takoma = {530,630} 
        phone = "2404502092" #is there a way we can hyper link this so when it prints on the screen thte app can just click 
        takoma_info = [bank_name_takoma,  phone, pref_pick_up_time]
        
        
class umd_food:
    def __init__(self, umd):
        '''initializing functions, variables,getting user input, combining inputs into lists for umd food bank'''
        bank_name_umd = "UMD Campus Pantry"
        address = "South Campus Dining Hall, 7093 Preinkert Dr, College Park, MD 20740"
        pref_pick_up_time_umd = {730,830} 
        phone = "3014059579"
        umd_info = [bank_name_umd,  phone, pref_pick_up_time]
        
       
def main(   ):
    '''acting as main. should be a loop for each time a new input is created, a new frat or soriority, regex functions limit user input to avoid errors in address, food input, name input, etc.'''
    frats_dict = {}
    sor_dict = {}
    print("welcome")
    x = input("To begin, please state if you represent either a Fraternity or Sorority?:")
    if x =="Fraternity":
        '''matching user input'''
        print("To begin, please enter your greek letters, if you are not in our system, we will add you:")
        Fname = input("Greek Letters: ")
        if Fname not in frats_dict:
            '''parsing thorugh dict to see if new entry needs to be added'''
            print("It appears you are not in our database, please enter your address like '123 Rocky Road'")
            Faddy = input()
            frats_dict.update({Fname:Faddy})
            Fraternity(Fname)
        exit()       
    elif x =="Sorority":
        print("To begin, please enter your greek letters, if you are not in our system, we will add you:")
        Sname = input("Greek Letters: ")
        if Sname not in sor_dict:
            '''parsing thorugh dict to see if new entry needs to be added'''
            print("It appears you are not in our database, please enter your address like '123 Rocky Road'")
            Saddy = input()
            frats_dict.update({Sname:Saddy})
            Sorority(Sname)
            exit()
    else:
        print("please try again")




def matching(self,umd,takoma,pac):
    '''comparing pickup times from soroiry/frat input to the times the food banks selected previously, printing matches'''
    if pick_up == pref_pick_up_time_umd:
        print("Your time input matches with", umd_info, "please contact for further drop off or pick up information")            
    elif pick_up == pref_pick_up_time_pac:
        print("Your time input matches with", pac_info, "please contact for further drop off or pick up information")
    elif pick_up == pref_pick_up_time_takoma:
        print("Your time input matches with", takoma_info, "please contact for further drop off or pick up information")       
    else:
        print("Try again, time input not valid")

if __name__ == "__main__":
    print("Please begin prompt to fufuil your order")
    start_var = Greek() 