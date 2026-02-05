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

