
#printing output of welcome message
print('Welcome to python pizza deliveres!')

# Taking the input of the pizza size for the user
size = input("What size pizza do you want? S, M, or L:").lower()

# Taking the input and ask for Y to add pepperoni and N to no add pepperani 
add_pepperoni = input("Do you want pepperani? Y or N:").lower()

# Taking the user input to add or not add the chesse 
extra_chess = input("Do you want extra chesse? Y or N:").lower()

# Tracking the bill of user
bill = 0

# if user select pizza size small then bill will be 15 doller
if size == "s":
    bill += 15

# if user select pizza size mediam then bill will be 20 doller    
elif size == "m":
    bill += 20

# if user select pizza size large then bill will be 25 doller
else:
    bill += 25

# if user select add pepperoni yes
if add_pepperoni == "y":

# add pepperoni is yes then the bill made what the user select the size to buy pizza
    if size == "s":

# if user choose pizza size 'small' and add pepperoni 'yes' then bill will be 15 + 2 = 17
        bill += 2

# if user choose pizza size "medium" or "large" and add pepperoni "yes " then bill will be for "m" 20 + 3 =23 and for "l" 25 + 3 = 28 
    elif size == "m" or size == "l":
        bill += 3
        
# if user want to add the extra chess without pippproni then bill adding the (user pizza size price + 1) and if they also want add pepperoni than bill will be size of pizza + add pepproni size + chess 
if extra_chess == "y":
    bill += 1


# finally after all input printing the totall bill
print(f"The total bill ${bill}")


