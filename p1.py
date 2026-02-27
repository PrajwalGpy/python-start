# name = "Prajwal"
# age = 20
# year = 2026

# print("hiii my name is " + name + " i am " + str(age) + " old " + " corrent year is " +  str(year)) 


# type casting

# print(type(8.90))
# print(type("45"))
# print(type(True))
# print(type(5))

# a = int(4.5)
# b = int("5")
# c = float(5)
# d = float("5")
# f = str(2.3)
# g = str(4)
# h = int(float("4.5"))

# print([a,b,c,d,f,g,h])


# item_name = "blurballs"
# item_price = 20.3
# item_contity = 30
# in_stock = True
# print(item_name,item_price,item_contity,in_stock)



# 🕹️ Arcade Day Pass Tracker — Challenge Steps
#
# 1) Create variables to store:
#    - customer name
#    - number of passes
#    - tokens per pass
#    - price per pass
#    - tokens required per game
#
# 2) Calculate:
#    - total tokens
#    - total cost
#    - games available  (use 'floor division' to get a whole number)
#
# 3) Print a summary with:
#    - customer name
#    - passes bought
#    - total tokens
#    - total cost
#    - games available



# customer_name = "Prajwal GP"
# number_of_passes = 5
# token_per_pass = 500
# price_per_pass = 10.5
# token_req_per_game = 100


# total_tokens =  token_per_pass * number_of_passes
# total_cost = number_of_passes * price_per_pass
# game_availabel = total_tokens / token_req_per_game 

# print("customer name :- " + customer_name)
# print("passes bought :- " + str(number_of_passes))
# print("total tokens :- " + str(total_tokens))
# print("total cost :- " + str(total_cost))
# print("games available :- " + str(game_availabel))


# user input

# name = input("Enter your name : ")
# age = input("Enter your age : ")

# print(f"hee {name} you are {age} old")

# num1 = float(input("Enter the first number :"))
# num2 = float(input("Enter the second number : "))


# value = num1 + num2
# print(value)


# - Create a distance converter converting Km to miles
# - Take two inputs from user: Their first name and the distance in km
# - Print: Greet user by name and show km, and mile values
# - 1 mile is 1.609 kilometers
# - hint: use correct types for calculating and print
# - Did you capitalize the name

# name = input("Enter the your name : ")
# distence = float(input("Enter your distance in km : "))
# km_in_miles = distence/1.609
# print(f"your name is {name.capitalize()} and the miles you are in {round(km_in_miles,2)}")


# a = 3
# b = 2

# print([a+b],[a-b],[a*b],[a/b],[a//b],[a%b],[a**b])


# msg = "welcome to Python 101: Strings"
# print(msg.upper())
# print(msg.lower())
# print(msg.capitalize())
# print(msg.title())

# print(len(msg))

# print(msg.count("o"))

# msg='welcome to Python 101: Strings'
# out = f"{msg[-10]} {msg[:7].capitalize()} { msg[25:29]} {msg[8:10]} {msg[13]+msg[12]+msg[2]+msg[1]+msg[-5]}"
# print(out.title())

# msg='welcome to Python 101: Strings'
# # print(msg.find("w"))
# print(msg.replace("101","Prajwal GP"))
# print( "Py" not in msg)

# name='TERRY'
# color = 'RED'

# print(f"{name.title()} loves the color {color.lower()}")




# 🏁 Pit Stop Timing Optimizer 🔧
#
# 1. Ask the user for the total race time in seconds.
# 2. Ask how many pit stops were made.
# 3. Ask for the average pit stop duration (in seconds).
#
# Then:
# - Calculate the total pit stop time.
# - Calculate the percentage of the race spent in the pits.
# - Round the percentage to 2 decimal places.
#
# Finally, print all of the following:
# - Total pit stop time in seconds
# - Percentage of race time spent in pits
# - A final message if pit time > 5% of the race: "You need a new pit crew. 🛠️"

# total_race_time = float(input("what is the total race time in seconds : "))
# total_stops = int(input("How many stop in the made : "))
# avg_stop_dur = float(input("Average pit stop duration :"))


# total_pit_stop_time = avg_stop_dur * total_stops
# per_spent_in_pit = round((total_pit_stop_time/total_race_time)*100,2)

# print("--------------------------------------------")
# print(f"Total pit stop time {total_pit_stop_time}")
# print(f"Percentage of race time spent in pits {per_spent_in_pit}")
# if per_spent_in_pit > 5 :
#     print("You need a new pit crew. 🛠️")


# friends = ['Prajwal','GP','Pajju','Pajju GP']

# print(friends[1])
# print(friends.index())


# friends = ['John','Michael','Terry','Eric','Graham']
# cars = [911,130,328,535,740,308]
# friends.sort()
# print(friends)
# cars.sort()
# print(cars)
# friends.sort(reverse=True)
# print(friends)

# print(max(cars))
# print(min(cars))

# friends.append("Prajwal") # insert value into the end of the list
# friends.insert(2,"GP")  # insert an value into specific position
# friends[0]= "gogo"
# friends.extend(cars) # combine to lists 
# print(friends)

# friends.remove('Eric')
# friends.pop()
# friends.pop(0)
# del friends[1]
# print(friends)


# new_friends = friends[:]
# new_friends = friends.copy()
# new_friends = list(friends)
# print(new_friends)


# sales_w1 = [7,3,42,19,15,35,9]
# sales_w2 = [12,4,26,10,7,28]
# sales = []

# lamanade = int(input("Enter the number of lemanade selled on this day : "))
# sales_w2.append(lamanade)
# sales_w1.extend(sales_w2)
# sales = list(sales_w1)
# print(sales)
# print("____________________________________")
# print(f"best earing {max(sales)*1.5}$")
# print(f"worst earing day {min(sales)*1.5}$")
# print(f"Total Profit is { sum(sales)*1.5}$")

# msg ='Welcome   to  Python  101: Split   and Join'
# csv = 'Eric,John,Michael,Terry,Graham'
# friends_list = ['Eric','John','Michael','Terry','Graham']

# print(msg.split())
# print(csv.split(','))
# print(" ".join(friends_list))

# print("-".join(msg.split()))

# print(msg.replace(" ",''))



# csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'
# friends_list = []
# print(friends_list)
# # From the list above fill a list(friends_list) properly
# # with the names of all the friends. One per "slot"
# # you may need to run same command several times
# # use print() statements to work your way through the exercise

# csv = csv.replace(":",",")
# csv = csv.replace(";",",")
# friends_list = list(csv.split(","))
# print(friends_list)


# friends = ["pgp","gp","jj","gojo"]
# friends_tuple = ("pgp","gp","jj","gojo")
# friends_set = {"pgp","gp","jj","gojo"}
# friends_set_2= {"pgp","gp","jj","gojo","jaady","nodes"}
# # friends = []
# # friends_tuple= tuple()
# # friends_set = set()

# print(friends_set.intersection(friends_set_2))
# print(friends_set_2.difference(friends_set))
# print(friends_set.union(friends_set_2))





#Sets - Exercise

#1. Check if ‘Eric’ and ‘John’ exist in friends
#2. combine or add the two sets 
#3. Find names that are in both sets
#4. find names that are only in friends
#5. Show only the names who only appear in one of the lists
#6. Create a new cars-list without duplicates

# friends = {'John','Michael','Terry','Eric','Graham'}
# my_friends = {'Reg','Loretta','Colin','John','Graham'}
# cars =['900','420','V70','911','996','V90','911','911','S','328','900']

# print('Eric' and 'John' in friends)

# print(friends.union(my_friends))

# print(friends.intersection(my_friends))

# print(friends.difference(my_friends))

# cars = set(cars)
# print(cars)



# def greeting(name,age=40):
#     print(f"heee you are {name} and you are {str(age)} old")

# name = input("Enter your name : ")
# age = input("Enter your age : ")

# if age:
#     greeting(name,age)
# else:
#     greeting(name)





# 1. Add new print statement - on a new line
#    which says 'We hear you like the color xxx! xxx is a string with color 
# 2. extend the function with another  input parameter 'color', that defaults to 'red'
# 3. Capture the color via an input box as variable:color 
# 4. Change the 'You are xx!' text to say 'you will be xx+1 years old next birthday 
#  adding 1 to the age
# 5. Capitalize first letter of the 'name', and rest are small caps 
# 6. Favorite color should be in lowercase 

# def greeting(name,color='red', age=28):
#     print(f"We hear you like the color {color.lower()}")
#     print(f"You are {name.capitalize()}!  you will be {int(age)+ 1} years old next birthday")
    
# color = input("Enter your fav color : ")
# name = input('Enter your name: ')
# age = input('Enter your age: ')
# greeting(name,color,age)




# def GrandTotal(amount):
#     total = amount * 10
#     rage = 20
#     return [total,rage]

# value = GrandTotal(amount=200)
# print(value[1],type(value))


# a = 2
# b = 7

# print(a>b)
# print(a<b)
# print(a!=b)
# print(a== b)
# print("a" in "ajji")
# print("a" not in "gjji")

# c = [1,2,3]
# d = [1,2,3]

# print(c == d)
# print( c is d)
# print(id(c),id(d))


# print('if elif else - Exercise')
# Create a calculator which handles +,-,*,/ and outputs answer based on the mode/ operator used
# Hint: use 3 separate inputs 
# Bonus: Extend functionality with extra mode so it also does celsius to fahrenheit conversion
# formula is: temp in C*9/5 + 32 = temp in f

# num1 =20
# num2 = 5
# operand = "-"
# temp = 68
# f = 0
# if temp :
#     f = temp*9/5+32

# result = 0
# if operand == "+":
#     result=  num1 + num2
# elif operand == "-":
#     result = num1 - num2
# elif operand == "*":
#     result = num1 * num2
# else :
#     result = num1 / num2
    
# print(result)
# print(f"temp is : {f}")






# def num_days(month):

#     if month in ['jan','mar','may','jul','oct','dec']:
#         print('number of days in',month,'is',31)
#     elif month == 'feb':
#         print('number of days in',month,'is',28)
#     elif month in ['apr','jun','sep','nov']:
#         print('number of days in',month,'is',30)
   

# num_days('jul')
# # optimize/shorten the code in the function
# # try to reduce the number of conditionals 


# i = 1
# while i <= 5:
#     print(f"{i}.{'*'*i}Loops are great{'*'*i}")
#     i = i+1



# print('Guessing game') 
# Guess the correct number in 3 guesses. If you don’t get it right after 3 guesses you lose the game. 
# Give user input box: 1. To capture guesses, 
# print(and input boxes) 1. If user wins 2. If user loses
# Tip:( remember you won’t see  print statements durng execution, so If you want to see prints during whle loop, then print to the input box

#Modification 1: number 1-100, tell user if guess is too high/low ,and let them have 5-10 guesses.
# Tip:( remember you won’t see  print statements during execution, so If you want to see prints during whle loop, print to the input box (This is specific to this platform)
# Three Loop Questions:
#1. What do I want to repeat?
#  -> 
#2. What do I want to change each time?
#  -> 
#3. How long should we repeat?
#  -> 

# guess = 3 
# value = 25
# while guess > 0:
#     guess -= 1
#     guess_value = int(input("Enter the guessing value : "))
#     if guess == 0 and guess_value != value:
#         print(f"your guess wrong and play the game again")
#     elif guess_value == value:
#         print(F"your guess is write {guess_value}")
#         break
#     elif guess_value > value:
#         print(f"your guess to heigh you only had {guess} left")
#     elif guess_value < value :
#         print(f"your guess to low you only had {guess} left")
    

# ☕ Coffee Order Queue Challenge
# 1. Set up two variables: one for total price, one for drink count
# 2. Start a while True loop
# 3. Ask for the customer's name
# 4. If the name is "done", break the loop
# 5. Ask for their drink order
# 6. If it's "latte", add 3.50 to total and +1 to drink count
#    If it's "americano", add 3.00 to total and +1 to drink count
#    If it's "espresso", add 2.50 to total and +1 to drink count
# 7. If it's not one of those drinks, print a warning and continue
# 8. After the loop, print total number of drinks and total price

# total_price = 0
# drink_count = 0

# while True:
#     name = input("Enter your name :(exit menu type done) :")
#     if name.lower() == "done":
#         break
#     drink_orders = input("What you want to drink (latte,americano,espresso) : ")
    
#     if drink_orders == "latte":
#         total_price += 3.50
#         drink_count += 1
#     elif drink_orders == "americano":
#         total_price += 3.00
#         drink_count += 1
#     elif drink_orders == "espresso":
#         total_price += 2.50
#         drink_count +=1
#     else:
#         print("order is not available")
        

# print("------------Bill-------------------")
# print(f"total number of drinks : {drink_count}")
# print(f"total Price is : {total_price}")

# for loop

# name = ['Pajju','rajju','sajju']

# for names in range(2):
#     for ju in name:
#         print(names,ju)


# names = ['john ClEEse','Eric IDLE','michael']
# names1 = ['graHam chapman', 'TERRY', 'terry jones']

# for name in range(2):
#     added_name = input("Enter the extra gests name : ")
#     names.append(added_name)



# all_gestes = names  + names1 


# for all_gust in all_gestes:
#     print(f"{all_gust.title()} You are invited to party for sunday!")
    
# 📱 Phone Number Formatter
#
# 1. Ask the user to enter a U.S. phone number in **any format**.
# 2. Use .strip() to remove any leading/trailing spaces.
# 3. Replace common separators (-, (, ), .) with spaces.
# 4. Use .split() to break into chunks, then .join() to merge the digits.
# 5. Check if the cleaned number has **exactly 10 digits**.
# 6. If yes, format it like this: (123) 456-7890
# 7. If not, print an error message: "Please enter exactly 10 digits."


# phone_number = input("Enter your phone number : ")
# phone_number = phone_number.strip()
# # phone_number = phone_number.replace('-',' ').replace('(',' ').replace(')',' ').replace('.',' ')

# for ch in ['-','(',')','.']:
#     phone_number = phone_number.replace(ch,' ')
    
# phone_number = ''.join(phone_number.split())

# if len(phone_number) == 10 :
#     print(f"({phone_number[:3]}) {phone_number[3:6]}-{phone_number[6:]}")
# else:
#     print("Please enter exactly 10 digits.")

# names = ['john ClEEse','Eric IDLE','michael']

# for name,ind in enumerate(names,5):
#     print(name,ind)

# num = [3,4,10,-2,3,5]
# # num.sort()
# # num.reverse()

# print(sorted(num,reverse=True))


# 🛂 Access Control Scanner Challenge
#
# 1. Create a set of revoked badge numbers.
# 2. Create two empty lists: "approved" and "denied".
# 3. Start a loop to collect visitor info:
#    - Ask for the visitor's name (or type "done" to finish).
#    - If the name is "done", exit the loop.
#    - Otherwise, ask for their badge number.
#    - Check if the badge is revoked:
#        • If revoked: add the name to "denied" and display "ACCESS DENIED".
#        • If not: add the name to "approved" and display "ACCESS GRANTED".
# 4. Print the final "Access Summary" for "✅ Approved Visitors" & "⛔️ Denied Visitors":
#    - Sort both lists alphabetically.
#    - Display the total number of approved and denied visitors.

 


# revoked_badge = [22,44,89.78,67,100]

# approved =[]
# denied = []

# while True :
#     name = input("Enter your name : (or type \"done\" to finish) : ")
#     if name.lower() == "done":
#         break
#     else:
#         badge_number = int(input("Enter your badge number : "))
        
#         if badge_number in revoked_badge:
#             denied.append(name)
#             print(f"{name} your access denied")
#         else:
#             approved.append(name)
#             print(f"{name} access granted")

# print("---------------------------------------------------------")
# print("✅ Approved Visitors \& ⛔️ Denied Visitors")
# sorted(approved)
# sorted(denied)
# print(f"✅ Approved Visitor")
# for approve in approved:
#     print(approve)
# print(f"the total approved is {len(approved)}")
# print(f"⛔️ Denied Visitors")
# for deniede in denied:
#     print(deniede)
# print(f"the total deniede is {len(denied)}")


# ☕️ Loyalty Points Engine Challenge
#
# RULES:
# • Each whole dollar spent earns 3 points
# • Tiers:
#     < 100 pts   →  Bronze
#     100-499 pts → Silver
#     ≥ 500 pts   →  Gold
#
# STEPS:
# 1. Define earn_points(price) → returns points for one purchase
# 2. Define tier_label(points) → returns "Bronze" / "Silver" / "Gold"
# 3. Given the hard-coded list `purchases`,
#    loop through it, call earn_points() for each amount,
#    and add the result to total_points.
# 4. After the loop, call tier_label(total_points)
# 5. Print 'Loyalty Summary':
#       • Total dollars spent
#       • Total points earned
#       • Final tier

# Purchase history (e.g., 3.75, 7.20, etc.)
# purchases = [4.5,6,20,1.8,100]

# def earn_points(price):
    
#      return price*3

# def tier_label(points):
#     if points < 100 :
#         return "Bronze"
#     elif points >= 100  and points < 499 :
#         return "Silver"
#     else:
#         return "Gold"
# total_points = 0
# for pur in purchases:
#     total_points += earn_points(price=pur)
# final_tier = tier_label(points=total_points)

# print('Loyalty Summary')

# print(f'Total dollars spent : {sum(purchases)}')
# print(f'Total points earned : {total_points}')
# print(f'Final tier : {final_tier}')
    
    
# movie  = {
#     'name' : 'gangubai',
#     'year': 2025,
#     'acters' : ['pajju','sajju','gajju']
    
# }
# # print(movie.get('name'))
# # movie['beget'] = 3000
# # print(movie)
# movie.pop('year')

# for key,value in movie.items():
#     print(key,value)


# 🐾 Dog Bus Tracker — Challenge Steps
#
# 1. Start with a bus dictionary holding current passengers.
#    - Each seat number (1, 2, 3, ...) is a key
#    - Each value is another dictionary with each pet's:
#        • name
#        • breed
#        • pickup time
#        • dropoff time
#
# 2. Print a starting roster showing each pet’s seat, name, and pickup time.
#
# 3. Add one new pet if there’s room on the bus.  
#    - Use MAX_SEATS to limit capacity.  
#    - Dynamically assign the next seat number.  
#    - Print the updated roster showing all pets after pickup.  
#
# 4. Ask which pet leaves early.  
#    - Remove that pet from the bus.  
#    - Print a message saying they’ve headed home.  
#
# 5. Print a final roster listing the remaining pets and their dropoff times.  

# MAX_SEATS = 4
# passengers = {
#     '1' : {'name':'Pjuu','breed':'lab','pickup':4.5,'dropoff':8},
#     '2':{'name':'rjju','breed':'lab','pickup':9.5,'dropoff':9},
#     '3':{'name':'Pjuu','breed':'lab','pickup':10.5,'dropoff':6}
# }

# for passe,value in passengers.items():
#     print(value['name'],passe,value['breed'],value['pickup'],value['dropoff'])

# next_seat = max(passengers)+1
    
#  if MAX_SEATS < next_seat :
#     # passengers.update({})



#It’s...not really an adventure game...#Ver 1.0
#Your village is being attacked by 'a germanic tribe' and you need to run to the stores and get the right things to save your village, and probably some good looking girl or boy you want to marry. All prices in gold pieces excl. VAT... chop chop!! ze germanz are coming!
#The code should allow you to get 1 thing from each store and each item you get should be removed from the store inventory, then do same for next store...
# one way to buy by typing the key 'newt' in an input box...or something
# at end you should print the 'items' you have taken..in this version you don't have to pay for stuff or add it up
#ver 1.2 add ability to exit a store without buying and go to next by typing 'exit', and to exit if a nonexistant item is bought(typed)
#Add purse with 1000 gold pieces and payment for the items during or at end of code and show a message about total cost and how much gold you have left
#ver 1.4 random bug fix, ' browser compatability', refactoring code... basically being lazy ..stop scrolling TikTok/Facebook! ;-)
#Ver 1.5 print inventory before and after purchases as one department_store of stuff(combine inventories from all stores into one...pretend Big Biz bought all the local stores, and want constant reporting for inventory management...)
# as in all games there is a special way to do this that actually makes money and solves the problem...can you find 'them'? Do you know why? May require knowledge of actual python 'lore'

# #create stores
# freelancers = {'name':'freelancing Shop','brian': 70, 'black knight':20, 'biccus diccus':100, 'grim reaper':500, 'minstrel':-15}
# antiques = {'name':'Antique Shop','french castle':400, 'wooden grail':3, 'scythe':150, 'catapult':75, 'german joke':5}
# pet_shop = {'name':'Pet Shop','blue parrot':10, 'white rabbit':5, 'newt': 2}

# cart = {}
# purse = 1000

# # Function to show inventory (merging on the fly)
# def get_inventory():
#     return freelancers | antiques | pet_shop

# print(f"Inventory before: {get_inventory()}")
# print("__________________________________________")

# for shop in (freelancers, antiques, pet_shop):
#     # Using .get() for the name so we don't accidentally buy the 'name' key
#     prompt = f"Welcome to {shop['name']}! (Purse: {purse})\n{shop}\nWhat do you want to buy? (type 'exit' to leave): "
#     item_name = input(prompt).lower().strip()
    
#     if item_name == 'exit':
#         continue # Moves to the next shop
    
#     if item_name not in shop or item_name == 'name':
#         print(f"Sorry, we don't have '{item_name}' here.")
#         continue
    
#     # Transfer the item
#     price = shop.pop(item_name)
#     cart.update({item_name: price})
#     purse -= price
#     print(f"Added {item_name} to cart for {price} gold.")

# # Final Summary
# total_spent = sum(cart.values())
# bought_items = ", ".join(cart.keys())

# print("__________________________________________")
# print(f"You Purchased: {bought_items}")
# print(f"Total spending: {total_spent} | Remaining gold: {purse}")
# print(f"Inventory after: {get_inventory()}")







# #create an dempty shopping cart
# cart = {}
# #loop through stores/dicts
# for LOOP OVER THE SHOPS :
#     #inputbox  to show what you can buy...capture textstring of what was bought...make lowercase
#     buy_item = input(f'Welcome to {SHOPNAME}! what do you want to buy: {LIST ITEMS FOR SALE})
#     #update the cart
#     cart.update({insert KEYVAL:VALUE}) # use pop...
# print(f'You Purchased {ITEMS PUCHASED} Today it is all free. Have a nice day of mayhem!')

# myfile = open('/home/prajwalgp/Downloads/pajju.txt','r')
# print(myfile.readlines())
# myfile.close()
# with open('/home/prajwalgp/Downloads/pajju.txt','r') as f :
#     print(f.read())



# try:
#     num = int(input("Enter an number betwenv 1 and 30 :"))
#     value = 30/num
# except ZeroDivisionError as err:
#     print(err,"you canot enter zero")
# except ValueError as err:
#     print(err,"value is not valid")
# except :
#     print("invalid value")
# else:
#     print(f"diviton is {value}")
# finally:
#     print("Thnaks for plalying")



# class movie:
#     def __init__(self,name,year,score):
#         self.name = name
#         self.year = year
#         self.score = score
        
#     def info(self):
#         print(f'Movie name : {self.name}')
#         print(f'Movie year : {self.year}')
#         print(f'Movie score : {self.score}')

# film1 = movie('gagan',2024,9.8)
# film2 = movie('raju',2026,7.8)

# print(film1.name,film1.year)
# film2.info()

# movie.info(film1)

# class Person:
#     def move(self):
#         print("move 4 step")
#     def rest(self):
#         print("heal 4 points")
        
# class Doctor(Person):
#     def heal(self):
#         print("Heal 10 points")
        
# class wizard(Doctor):
#     def magic(self):
#         print("Deal magic damage")   
#     def heal(self):
#         print('heal 15 points')

# char1 = Person()
# # char1.move()
# # char1.rest()

# char2 = Doctor()

# # char2.heal()
# # char2.move()
    
# char3 = wizard()

# char3.magic()
# char3.heal()  


#  🍕 Pizza Builder — Challenge Steps
#
# 1. Define a Pizza class that stores:
#    - size, crust type, and a list of toppings
# 2. Add a method to add a new topping
# 3. Add a method to remove a topping if it exists
# 4. Add a method to print pizza details:
#    - size, crust, and all toppings (or “No toppings yet!”)
# 5. Create a pizza object, customize it, and print the summary

# class Pizza:
    
#     def __init__(self,size,crust_type,list_of_toppings=None):
#         self.size = size
#         self.crust_type = crust_type
#         self.list_of_toppings = list_of_toppings if list_of_toppings else []
    
    
#     def add_new_topping(self,new_toppings):
#         if isinstance(new_toppings,list):
#             self.list_of_toppings.extend(new_toppings)
#         else:
#             self.list_of_toppings.append(new_toppings)

    
#     def remove_toppings(self,toppings):
#         if toppings in self.list_of_toppings :
#             self.list_of_toppings.remove(toppings)
#         else:
#             print(f"{toppings} didn't exits")
    
#     def display(self):
#         print("🍕 --------Your Pizza Details--------------")
#         print(f"Size : {self.size.title()}")
#         print(f"crust : {self.crust_type.title()}")
#         if self.list_of_toppings :
#             print("Toppings")
#             for num,toppings in enumerate(self.list_of_toppings,1):
#                 print(f"{num}. {toppings.title()}")
#         else:
#             print("No Toppings")

# myPizza = Pizza("small","deep")
# myPizza.add_new_topping(["onions","salad"])
# myPizza.add_new_topping("berry")
# myPizza.remove_toppings("salad")
# myPizza.remove_toppings("pajju")
# myPizza.display()


# import random as rand
# my_numbers = [10, 20, 30, 40, 50]
# choi = rand.choice(my_numbers)
# print(choi)

# num = '1234'
# car = ['rajju','ggajju','sajju']

# dog = zip(num,car)
# print(dog)

# bed,no = zip(*dog)
# bed= list(bed)
# print(bed,no)


# print('Lambdas Exercise')

# def f(x): return x + 5
# f = lambda x,y: x+y
# print(f(2,4))

# def strip_spaces(str):
#    return ''.join(str.split(' '))
# #write equivalent lambda and insert Lambda here
# strip_spaces1 = lambda str : ''.join(str.split(' '))
# print(strip_spaces1('Monty Pythons Flying Circus')) 

# def join_list_no_duplicates(list_a,list_b):
#    return list(set(list_a + list_b))
# list_a = [1,2,3,4]
# list_b = [3,4,5,6,7]
# #write lambda below 
# join_list_no_duplicates1 = lambda list_a,list_b : list(set(list_a + list_b))
# print(join_list_no_duplicates1(list_a,list_b))

#Complete the function so it returns a function
# def create_quad_func(a,b,c):
#     '''return function f(x) = ax^2 + bx + c'''
#     return lambda x: a*x**2 + b*x + c
# f = create_quad_func(2,4,6)
# g = create_quad_func(5,6,7)
# print(f(2))
# print(g(2))

# signups = ['MPF104', 'MPF20', 'MPF2', 'MPF17', 'MPF3', 'MPF45']
# # print(sorted(signups)) # Lexicographic sort
# #write sorting by integer
# print(sorted(signups,key= lambda id:int(id[3:]))) # Integer sort



# import random as rand


# for  i in range(5):
#     print(rand.uniform(1,100))

# # print(dir(rand))


# goo = ["goo","ewiue","woewhe","Pakke"]

# rand.choice(goo)
# print(rand.choice(goo))



# 🏆 Raffle Prize Picker — Challenge Steps
#
# 1. Ask how many people are entering the raffle (at least 3 names).
# 2. Use a loop to collect their names into a list.
# 3. Ask for exactly 3 prize names (in order) and store them in a list.
# 4. Randomly pick 3 different winners from the participant list.
# 5. Print out who wins which prize and make sure the final one
#    is clearly marked as the Grand Prize. 🏆
#
# Hint: Use loops, lists, and a tool that picks random items without repeats.

# import random as rand

# participants = []

# while True:
#     name = input("Enter your name : ")
#     if name == "done":
#         break
#     else:
#         participants.append(name)
    
# prize = ["1 k","40 k","1lac R"]

# winners = rand.sample(participants,3)

# for i in range(3):
#     if i == 2 :
#         print(f" grand winner prie is  : {winners[i]} prize is {prize[i]}")
#     else:
#         print(f" other winner are {winners[i]}  prize is {prize[i]}")


# import random as rand
# print('Project - Math Tutor')


# pract_que = int(input("Enter the number of practice quetions : "))
# playe = {}
# for i in range(1,pract_que+1):
#     num1 = rand.randint(1,100)
#     num2 = rand.randint(1,100)
#     operands = ['+','-','*','/']
#     operand = rand.choice(operands)
#     if operand == "+" :  writeanwer = num1 + num2
#     elif operand == "-" :  writeanwer = num1 - num2
#     elif operand == "*" :  writeanwer = num1 * num2
#     else :   writeanwer = num1 / num2
   
#     useranswer = int(input(f"{i}. {num1}{operand}{num2} = "))
#     if useranswer == writeanwer:
#         playe[i] = True
#     else:
#         playe[i] = False
     
# count_wriht = 0   
# for key,values in playe.items():
#     if values == True  :
#         count_wriht += 1
        

# print("Thankyou for playing the game")
# print(F"total quetions correctly ansewerd are {count_wriht}")
# print(f"the the perchentage of rite answe is {count_wriht/pract_que*100} %")



# import random as rand

# print('--- Project: Optimized Math Tutor ---')

# # Use a try-except block to prevent the program from crashing if a user types a letter
# try:
#     pract_que = int(input("Enter the number of practice questions: "))
# except ValueError:
#     print("Please enter a valid number next time!")
#     exit()

# playe = {}
# operands = ['+', '-', '*', '/']

# for i in range(1, pract_que + 1):
#     num1, num2 = rand.randint(1, 100), rand.randint(1, 100)
#     operand = rand.choice(operands)
    
#     # Optimization: Use an f-string to build the math expression
#     expression = f"{num1} {operand} {num2}"
    
#     # Optimization: eval() can calculate a string, but for safety/practice
#     # we'll stick to a clean conditional or use the operator module.
#     if operand == "+":   correct_ans = num1 + num2
#     elif operand == "-":  correct_ans = num1 - num2
#     elif operand == "*":  correct_ans = num1 * num2
#     else:                 
#         # For division, we round to 2 decimal places to make it fair
#         correct_ans = round(num1 / num2, 2)
#         print("(Round your answer to 2 decimal places)")

#     try:
#         user_input = input(f"{i}. {expression} = ")
#         user_answer = float(user_input) # Use float so division answers work
        
#         # Store result directly in the dictionary
#         playe[i] = (user_answer == correct_ans)
        
#         if not playe[i]:
#             print(f"  ❌ Incorrect. The answer was {correct_ans}")
#     except ValueError:
#         playe[i] = False
#         print("  ❌ Invalid input. Marked as wrong.")

# # Optimization: You don't need a loop to count True values!
# # In Python, True equals 1 and False equals 0.
# count_right = sum(playe.values())
# percentage = (count_right / pract_que) * 100

# print("\n" + "="*20)
# print("Thank you for playing!")
# print(f"Total correct: {count_right}/{pract_que}")
# print(f"Grade: {percentage:.2f}%") # :.2f limits the decimal places in the printout

# print('Project - Trading game simulation / pseudo code')
# 
# import random as rand
# 
# bag = ["green","green","green","green","green","green","red","red","red","red"]
# rand.shuffle(bag)
# print(bag)
# valet = 1000
# corent_valet = 1000
# 
# rounds = int(input("Enter the how many rounds you whants to play : "))
# 
# for i in range(rounds):
    # rand.shuffle(bag)
    # bet_amount = int(input("Enter how much amount you will going to enter : "))
    # value = rand.choice(bag)
    # 
    # if (valet/2) > corent_valet :
        # print("you have low amount")
        # break
    # if corent_valet :
        # if value == "green":
            # corent_valet +=  bet_amount
            # print(f"you got {value} boll you won total {corent_valet}")
        # else:
            # corent_valet -= bet_amount
            # print(f"you got {value} boll you won total {corent_valet}")
    # else: 
        # if value == "green":
            # corent_valet = valet + bet_amount
            # print(f"you got {value} boll you won total {corent_valet}")
        # else:
            # corent_valet -= bet_amount
            # print(f"you got {value} boll you won total {corent_valet}")
    # 
# print("hiii how are  you")
# 
