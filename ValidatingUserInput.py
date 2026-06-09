# def user_choice():
#     #? Variables

#     #? Initial values
#     choice = ''
#     acceptable_range = range(0,10)
#     within_range = False

#     #? Two Condition to check 
#     #? Digit OR Within range value
#     while choice.isdigit() == False or within_range == False:
#         choice = input("Please Enter a number b/w(0-10): ")

#         #? Digit checker 
#         if choice.isdigit() == False:
#             print("Sorry that is not a digit\n  " \
#             "Please enter a valid input")

#             #? Range checker 
#         if choice.isdigit() == True:
#             if int(choice) in acceptable_range:
#                within_range = True
#             else:
#                 print("Sorry you are out of acceptable_range(0-10)")
#                 within_range = False
#     return int(choice)
# result = user_choice()
# print(result)



def user_choice():
    #? multiple variables

    #? Initial vlaues
    choice = "Wrogn"
    Acceptable_range = range(0,10)
    within_range = False

    #? we are going to two condition
    #? Is Number or Value within range
    while choice.isdigit() == False or within_range == False:
         #? user input 
        choice = input("Enter your choice: ")
        
        #? digit checker 
        if choice.isdigit() == False:
            print("Sorry i'ts not a digit!\n" \
            "Enter vailid number.")
        
        #? Range checker 
        if choice.isdigit() == True:
            if int(choice) in Acceptable_range:
                within_range = True
            else:
                print("Your choice is out of bond!\n" \
                "plz choose number within range(0,9).")

    return int(choice)
result = user_choice()
print(result)

