print("Hello! Welcome back to your comic book collection\n")

comicBooks = {"Miracle Man": 1, "Superman": 24}

for key, value in comicBooks.items():
    print(key, value)
print("\n")

print("Please select an option from the menu below\n") #introduction to program
userChoice = input(" Home | Add Comic | Remove Comic | Lists | Search | Help | Quit \n")

while (userChoice != 'Quit'): #begins while loop so user can continue to access different menu options
    if userChoice == "Home": # home menu option, displays comic collection
        print("Heck yeah, brah. Check out your sick comic books\n")
        for key, value in comicBooks.items():
            print(key, value)
        print("Please select an option from the menu below\n")
        userChoice = input(" Home | Add Comic | Remove Comic | Lists | Search | Help | Quit \n")

    elif userChoice == "Add Comic": # add comic option, displays prompts to add more comics to collection
        newIssues = int(input(print("Got some sweet new issues? Sick brah, how many new issues do you want to enter? ")))
        for i in range(newIssues): # for loop that tells program how many new comics will be added
            key = input("Enter comic title: ")
            value = int(input("Enter issue no.: "))
            comicBooks[key] = value
        print("Please select an option from the menu below\n")
        userChoice = input(" Home | Add Comic | Remove Comic | Lists | Search | Help | Quit \n")

    elif userChoice == "Remove Comic": # gives user option to remove comic from collection
        print("Sad day to be shrinkin' your comic collection, brah.\n")
        comicToBeRemoved = input("Which comic do you want to remove? ")
        del comicBooks[comicToBeRemoved]
        print("I never liked that comic anyways, brah.\n")
        print("Please select an option from the menu below\n")
        userChoice = input(" Home | Add Comic | Remove Comic | Lists | Search | Help | Quit \n")     
    
    elif userChoice == "Search": # gives user option to search through collection
        searchComics = input("What are you lookin' for brah? We probably got it\n")
        for key in comicBooks.items():
            if key == searchComics:
                print(key, value)
        print("Finished searchin, brah. Like what you see?\n")
        print("Please select an option from the menu below\n")
        userChoice = input(" Home | Add Comic | Remove Comic | Lists | Search | Help | Quit \n")

    # elif userChoice == "Lists":

    elif userChoice == "Help": # displays what each option does
        print("Home: Allows user to view current comic collection\n")
        print("Add Comic: Allows user to add comics to collection. Input comic title, then comic issue number. Easy difficulty.\n")
        print("Remove Comic: Allows user to delete comic from collection. Input comic title to delete. Easy difficulty.\n")
        print("Lists: Allows users to create individual lists of their collection. Intermediate difficulty.\n")
        print("Search: Allows user the ability to search comic collection. Input comic title to search. Easy difficulty.\n")
        print("Quit: Allows user to quit the program\n")
        print("Please select an option from the menu below\n")
        userChoice = input(" Home | Add Comic | Remove Comic | Lists | Search | Help | Quit \n")
    
    elif userChoice == "Quit": # allows user to quit program
        print("See you next time, brah. Your comic book treasures are safe with me.\n")

    else: # in case there is a typo or something give the options again
        print("Uh oh brah, seems like you didn't pick one of my preapproved options\n")
        print("Please select an option from the menu below\n")
        userChoice = input(" Home | Add Comic | Remove Comic | Lists | Search | Help | Quit \n")

