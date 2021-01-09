
# Welcome
print('Welcome to the Windalyzer - Wind Analysis Program!')

# Import libraries and helping functions
import numpy as np
# Import our own helping functions


# Mikkel's helping functions
from displayMenu import displayMenu #The displayMenu function is made by Mikkel N. Schmidt. See the function discription for more information. 
from inputNumber import inputNumber #The inputNumber function is made by Mikkel N. Schmidt. See the function discription for more information. 


# The different menu options and lists of text
menuOptions = np.array(['Load Data', 'Display statistics', 'Generate plots', 'Quit'])



# An infinite loop runs until the User chooses to Quit the program,
# in which case the loop Breaks. 
while True:
    # Start of program
    # The menu appears and asks the user to select an option
    print('\n------------Main menu------------\n')
    
    selection = displayMenu(menuOptions) 
    
    
    
    if selection == 1: # Choose Lindenmayer system and iterations
        pass
    elif selection == 2: # Generate plots
        if not len(LindString):
            print("Error. Please choose a system first")
            continue
        print('\nDo you like colors?')
        colorStyle = displayMenu(plotOptions)
        
    elif selection == 3: # Display Statistics
        if not len(LindString):
            print("Error. Please choose a system first")
            continue
        
        
        print('\n-----------Statistics-----------\n')
        print('Current Lindenmayer system: {}\nNumber of iterations: {}\n'.format(System,N))
        
        print("The total number of line segments are",sum(turtleCommands == lineLength))
        print("The total length of the curve is",round(sum(turtleCommands[turtleCommands == lineLength]),3))
        print("The total number of left turns are",sum((turtleCommands != lineLength)&(turtleCommands>0)))
        print("The total number of right turns are",sum((turtleCommands != lineLength)&(turtleCommands<0)))
        input('Press enter to return to Main Menu... ')
    elif selection == 4: # Quit program
        print('Thank you for using Windalyzer!\nWe hope to see you again soon!')
        break
    