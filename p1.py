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

name = input("Enter the your name : ")
distence = float(input("Enter your distance in km : "))
km_in_miles = distence/1.609
print(f"your name is {name.capitalize()} and the miles you are in {round(km_in_miles,2)}")

