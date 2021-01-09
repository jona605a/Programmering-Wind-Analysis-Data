
# Welcome
print('Welcome to the Windalyzer - Wind Analysis Program!')

# Import libraries and helping functions
import numpy as np
import os
# Import our own helping functions
from loadfuncs import dataLoad
from plotfuncs import (dataPlot)
from dataStatistics import dataStatistics

# Mikkel's helping functions
from displayMenu import displayMenu #The displayMenu function is made by Mikkel N. Schmidt. See the function discription for more information. 
from inputNumber import inputNumber, get_int_in_range #The inputNumber function is made by Mikkel N. Schmidt. See the function discription for more information. 


# The different menu options and lists of text
menuOptions = np.array(['Load Data', 'Display statistics', 'Generate plots', 'Quit'])
statisticsOptions = np.array(['Mean', 'Variance', 'Cross Correlation'])
plotOptions = np.array(['Contour', 'Surface'])

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
            filename = input('Please enter a correct filename for the data (turbine_32x32x8192.bin)\n or press "q" to escape: ')
            if filename == 'q':
                    break
            elif not os.path.exists(filename): # turbine_32x32x8192.bin
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
            print('\nError. Please load data first')
            continue
        
        print('\n------------Display Statistics------------\n')
        print('Which statistic do you want to display?')
        
        stat_selection = displayMenu(statisticsOptions)
        statistic = statisticsOptions[stat_selection-1]
        
        # Get the desired y and z value
        y = get_int_in_range('Please enter a value for y: ', 1, ranges[1])
        z = get_int_in_range('Please enter a value for z: ', 1, ranges[2])
        
        if statistic in ['Mean', 'Variance']:
            # Calculate the statistic
            Myz = dataStatistics(data, statistic)
            
            # Print to the user
            print('The {} of the data, where y = {} and z = {}'.format(statistic, y,z))
            print('\n', Myz[y, z])
        elif statistic == 'Cross Correlation':
            # Inquire about additional information
            yref = get_int_in_range('Please enter a value for Yref: ', 1, ranges[1])
            zref = get_int_in_range('Please enter a value for Zref: ', 1, ranges[2])
            DeltaX = get_int_in_range('Please enter a value for DeltaX: ', 1, ranges[0]-1)
            
            # Calculate the statistic
            Myz = dataStatistics(data, statistic, yref, zref, DeltaX)
            
            # Print to the user
            print('The {} of the data, where y = {} and z = {}, \n Yref = {}, Zref = {} and DeltaX = {}'.format(statistic, y, z, yref, zref, DeltaX))
            print('\n', Myz[y, z])
        
        
        
        
    elif selection == 3: # Generate plots
        if not len(data):
            print("Error. Please load data first")
            continue
        
        print('\n------------Generate plots------------\n')
        print('Which statistic do you want to plot?')
        
        stat_selection = displayMenu(statisticsOptions)
        statistic = statisticsOptions[stat_selection - 1]
        
        plotoptions = [statistic, ranges]
        
        print('\nWhat kind of plot do you want?')
        plot_selection = displayMenu(plotOptions)
        # Either 'Contour' or 'Surface'
        plotoptions.append(plotOptions[plot_selection - 1]) 
        
        if statistic == 'Cross Correlation':
            plotoptions.append( get_int_in_range('Please enter a value for Yref: ', 1, ranges[1]) )
            plotoptions.append( get_int_in_range('Please enter a value for Zref: ', 1, ranges[2]) )
            plotoptions.append( get_int_in_range('Please enter a value for DeltaX: ', 1, ranges[0]-1) )
        
        
        dataPlot(data, *plotoptions)
        
        
    elif selection == 4: # Quit program
        print('Thank you for using Windalyzer!\nWe hope to see you again soon!')
        break
    