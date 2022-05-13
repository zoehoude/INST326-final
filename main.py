


import re
"""Classes

    Class Greek stores the Chapter's donation order"""

class Greek:
    
    def order(key):
        
        """order is the stored donation"""
        
        order = {'entree': "empty", 'sides': "empty", 'packaged': "empty", 'serving_weight': 0, 'time': 0}
        
        entree = input("What is the main course?")
        sides = input("What are the sides to go with?")
        packaged = input("Is the item packaged? (Y/N)")
        serving_weight = input("Total Weight of Donation?")
        time = input("\nSelect a pick up time \n(5:30-6:30) or (6:30-7:30) or (7:30-8:30)\nInput 1, 2, or 3 accordingly\n")
        
        """appending the dictionary to order"""
        order['entree'] = entree
        order['sides'] = sides
        order['packaged'] = packaged
        order['serving_weight'] = serving_weight
        order['time'] = time
        return order
        
    
        
    
"""three sample Class service centers"""    
class preg_aid_center:
    def info():
        pac_data = {}
        '''initializing functions, variables,getting user input, combining inputs into lists for pac'''
        bank_name_pac = "Pregnancy Aid Center INC - Food Distribution Center"
        address = "4809 Greenbelt Rd, College Park, MD 20740"
        only_time = 1
        phone = "3014119150"
        maxlbs = 20
        pac_data['name'] = bank_name_pac
        pac_data['address'] = address
        pac_data['time Available'] = only_time
        pac_data['contact'] = phone
        pac_data['Weight Limit'] = maxlbs
        return pac_data
    

        
class takoma_park_food:
    def info():
        takoma_data ={}
        
        
        '''initializing functions, variables,getting user input, combining inputs into lists for takoma'''
        bank_name_takoma = "Takoma Park Food Pantry"
        address = "7001 New Hampshire Ave, Takoma Park, MD 20912"
        only_time = 2
        phone = "2404502092" 
        maxlbs = 30
        takoma_data['name'] = bank_name_takoma
        takoma_data['address'] = address
        takoma_data['time Available'] = only_time
        takoma_data['contact'] = phone
        takoma_data['Weight Limit'] = maxlbs
        return takoma_data
      
        
class umd_food:
    def info():
        umd_data = {}
        '''initializing functions, variables,getting user input, combining inputs into lists for umd food bank'''
        bank_name_umd = "UMD Campus Pantry"
        address = "South Campus Dining Hall, 7093 Preinkert Dr, College Park, MD 20740"
        only_time = 3
        phone = "3014059579"
        maxlbs = 100
        umd_data['name'] = bank_name_umd
        umd_data['address'] = address
        umd_data['time Available'] = only_time
        umd_data['contact'] = phone
        umd_data['Weight Limit'] = maxlbs
        return umd_data
    
       
        
    
    
"""functions conditions and confirm order"""  

    
def main():
    loop = True
    while loop == True:
        frats ={}
        sor = {}
        x = input("Welcome to GreekFeeds, a non-profit with the purpose of donating left-over food from Greek Life Chapters.\n To begin please state whether you represent a Fraternity of Sorority:")
    
        if x == "Fraternity":
            f = input("Hello Brothers, \nTo begin type in your chapter letters: ")
            while f not in frats:
                Faddy = input("It appears this is your first!\nLets add you in our system for the future. Enter your address:")
                frats[f] = Faddy
            
            fchoice = input("Would you like to continue to a donation or back to home? (yes or no)")
            if fchoice =="yes":
                    
                break
            else:
                continue
                   
        elif x == "Sorority":
            s = input("Hello Sisters, \nTo begin type in your chapter letters: ")
            if s not in sor:
                Saddy = input("It appears this is your first!\nLets add you in our system for the future. Enter your address:")
                sor[s] = Saddy
                schoice = input("Would you like to continue to a donation or add another chapter? (yes or no)")
                if schoice =="yes":
                    break
                    
                else:
                   continue
        else:
            print("Could be a typo. Retry using Sorority or Fraternity ")
            
        break    
     
    order = Greek.order(f)
    oTime = order.get('time')
    oWeight = order.get('serving_weight')
    oTime = int(oTime)
    oWeight = int(oWeight)
    
    
    
   
    return order, oTime, oWeight, frats, sor
    
    
def conditions(weight, time):
    pac = preg_aid_center.info()
    tak = takoma_park_food.info()
    umd = umd_food.info()
    
    
    
    if (weight <= 20 and time == 1):
        return pac 
    elif (weight <= 30 and time == 2):
        return tak  
    elif (weight <= 100 and time == 3):
        return umd
    
    else:
        error = 0
        
        return error
    


def confirm_order(orderdict, chardict):
    entree = orderdict.get('entree')
    sides = orderdict.get('sides')
    packaged = orderdict.get('packaged')
    weight = orderdict.get('serving_weight')
    time = orderdict.get('time')
    
    cname = chardict.get('name')
    caddy =chardict.get('address')
    ccontact = chardict.get('contact')
    written = print("Your order of " + entree + " with the sides of " + sides+ ", weighing at " + weight +" lbs"+"\nWill be picked up by "+cname+ " and brought to the address of "+caddy+ "at time "+time+"\nIf you have any questions please contact "+ccontact +"\n Time Key: 1 = 5:30-6:30pm, 2 = 6:30-7:00pm, 3 = 7:30pm - 8:30pm")
    return written

    

    
""" MAIN statement"""
       
if __name__ == "__main__":
    
    mainz = main()
    current_ords =mainz[0]
    time = mainz[1]
    weight = mainz[2]
    fratsdict = mainz[3]
    sordict = mainz[4]
    con = conditions(weight, time)
    fin = confirm_order(current_ords, con)
    
    
    
    
    
    
"""TEST CASES"""  

def test_conditions_pac():
    assert conditions(10, 1) == preg_aid_center.info()
    
def test_conditions_tak():
    assert conditions(20, 2) == takoma_park_food.info()
    
def test_conditions_umd():
    assert conditions(80, 3) == umd_food.info()

def test_conditions_error():
    assert conditions(400,3) == 0
    
test_conditions_pac()
test_conditions_tak()
test_conditions_umd()
test_conditions_error()



    
    
   
            
    

    
        
    
   
    
        
    
    
   
       
    
    
    
    
    
    
        
         
            
            
        
    
        