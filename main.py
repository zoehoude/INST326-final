
import re

class Greek:
    def __init__(self):
        """order is the stored donation"""
        order = {'entree': "empty", 'sides': "empty", 'packaged': "empty", 'serving_weight': 0, 'time': 0}
        entree = input("What is the main course?")
        sides = input("What are the sides to go with?")
        packaged = input("Is the item packaged and ready for storage? (Y/N)")
        serving_weight = input("Total Weight of Donation?")
        time = input("Select a pick up time /n(5:30-6:30) or (6:30-7:30) or (7:30-8:30)/nInput 1, 2, or 3 accordingly")
        
        """appending the dictionary to order"""
        order['entree'] = entree
        order['sides'] = sides
        order['packaged'] = packaged
        order['serving_weight'] = serving_weight
        order['time'] = time
        return order
    
"""three sample service centers"""    
class preg_aid_center:
    def __init__(self, pac):
        pac_data = {}
        '''initializing functions, variables,getting user input, combining inputs into lists for pac'''
        bank_name_pac = "Pregnancy Aid Center INC - Food Distribution Center"
        address = "4809 Greenbelt Rd, College Park, MD 20740"
        only_time = "5:30-6:30"
        phone = "3014119150"
        pac_data['name'] = bank_name_pac
        pac_data['address'] = address
        pac_data['time Available'] = only_time
        pac_data['contact'] = phone
        return pac_data
 
        
class takoma_park_food:
    def __init__(self, takoma):
        takoma_data = {}
        '''initializing functions, variables,getting user input, combining inputs into lists for takoma'''
        bank_name_takoma = "Takoma Park Food Pantry"
        address = "7001 New Hampshire Ave, Takoma Park, MD 20912"
        only_time = "6:30-7:30"
        phone = "2404502092" 
        takoma_data['name'] = bank_name_takoma
        takoma_data['address'] = address
        takoma_data['time Available'] = only_time
        takoma_data['contact'] = phone
        return takoma_data
        
        
class umd_food:
    def __init__(self, umd):
        umd_data = {}
        '''initializing functions, variables,getting user input, combining inputs into lists for umd food bank'''
        bank_name_umd = "UMD Campus Pantry"
        address = "South Campus Dining Hall, 7093 Preinkert Dr, College Park, MD 20740"
        only_time = {730,830} 
        phone = "3014059579"
        umd_data['name'] = bank_name_umd
        umd_data['address'] = address
        umd_data['time Available'] = only_time
        umd_data['contact'] = phone
        return umd_data
    
    
def conditions(order, centers)




#i know youre changing the idea but this is a stucture we can use
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

        #instance variable shoudl run through greek entity
if __name__ == "__main__":
    print("Please begin prompt to fufuil your order")
    start_var = Greek() 
        
        
