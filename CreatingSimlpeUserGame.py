
#? This function for index choose
def position_choice(my_lst):
    #? Initial condition
    choice = "Wrong"
    #? To checke is vailid
    while choice not in ['0','1','2']:
        #? User input
        choice = input("Pick a position (0,1,2): ")
        #? If choice is wrong 
        if choice not in ["0","1","2"]:
            print("Ooops its a invailid choice!\n"
            "choose a vailid number: ")
    return (int(choice))

#? This function for replacement
def replacement_choice(my_lst,index):
    #? input which you want to replace
    User_placement = input("Type a string to place at position: ")
    my_lst[index] = User_placement
    return my_lst

#? This function for game keepping on
def gameon_choice():
    #? Initial condition
    choice = "Wrong"
    #? To checke is vailid
    while choice not in ['Y','N']:
        #? User input
        choice = input("Keep playing? (Y or N): ").upper()
        #? If choice is wrong 
        if choice not in ['Y','N']:
            print("Ooops its a invailid choice!\n"
            "Plz choose Y or N: ")
        if choice == 'Y':
            return True
        elif choice == 'N':
            return False      

#? This function for displaying result
def display_game(my_lst):
    #? print current list
    print("Here is the current list")
    print(my_lst)
#? thid is input lst
my_lst = [0,1,2]
#! combine all function
game_on = True
while game_on:
    display_game(my_lst)
    position = position_choice(my_lst)
    replacement_choice(my_lst,position)
    display_game(my_lst)
    game_on = gameon_choice()
print("Game Over!")