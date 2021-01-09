
# Welcome
print('Welcome to the Windalyzer - Wind Analysis Program!')

# Import libraries and helping functions
import numpy as np
import os
# Import our own helping functions
from loadfuncs import dataLoad
from plotfuncs import (dataPlot)
import dataStatistics

# Mikkel's helping functions
from displayMenu import displayMenu #The displayMenu function is made by Mikkel N. Schmidt. See the function discription for more information. 
from inputNumber import inputNumber, get_int_in_range #The inputNumber function is made by Mikkel N. Schmidt. See the function discription for more information. 


# The different menu options and lists of text
menuOptions = np.array(['Load Data', 'Display statistics', 'Generate plots', 'Quit'])
statisticsOptions = np.array(['Mean', 'Variance', 'Cross Correlation'])

data = []

# An infinite loop runs until the User chooses to Quit the program,
# in which case the loop Breaks. 
while True:
    # Start of program
    # The menu appears and asks the user to select an option
    print('\n------------Main menu------------\n')
    
    selection = displayMenu(menuOptions) 
    
    
    if selection == 1: # Load wind data
        
        while True:
            filename = input('Please enter a correct filename\nfor the data or press "q" to escape: ')
            if filename == 'q':
                    break
            elif not os.path.exists(filename):
                print('\nInvalid filename')
            else:
                ranges = ['Nx', 'Ny', 'Nz']
                for i, val in enumerate(ranges):
                    ranges[i] = get_int_in_range('Please enter the value for '+ val+ ': ', 1, 1e9)
                data, errormessage = dataLoad(filename, *ranges)
                if errormessage != 'No error':
                    print ('\n'+errormessage)
                break
            
        
    elif selection == 2: # Display Statistics
        if not len(data):
            print("Error. Please load data first")
            continue
        
        stat_selection = displayMenu(statisticsOptions)
        statistic = statisticsOptions[stat_selection-1]
        
        # Get the desired y and z value
        y = get_int_in_range('Please enter a value for y: ', 1, ranges[1])
        z = get_int_in_range('Please enter a value for z: ', 1, ranges[2])
        
        if statistic in ['Mean', 'Variance']:
            Myz = dataStatistics(data, statistic)
            print('The % of the data, where y = % and z = %' % (statistic, y,z))
            print('\n', Myz[y, z])
        elif statistic == 'Cross Correlation':
            pass
        
        
        
    elif selection == 3: # Generate plots
        if not len(data):
            print("Error. Please load data first")
            continue
        print('\nDo you like colors?')
        colorStyle = displayMenu(plotOptions)
        
        
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
    