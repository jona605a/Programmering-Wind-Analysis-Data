
# Welcome
print('Welcome to the Windalyzer - Wind Analysis Program!')

# Import libraries and helping functions
import numpy as np
import os
import pandas as pd
# Import our own helping functions
from loadfuncs import dataLoad
from plotfuncs import (dataPlot)
from dataStatistics import dataStatistics

# Mikkel's helping functions
from displayMenu import displayMenu #The displayMenu function is made by Mikkel N. Schmidt. See the function discription for more information.
from inputNumber import inputNumber, get_int_in_range #The inputNumber function is made by Mikkel N. Schmidt. See the function discription for more information.


# The different menu options and lists of text
menuOptions = np.array(['Load Data', 'Display statistics', 'Generate plots', 'Quit'])
statisticsOptions = np.array(['Mean', 'Variance', 'Standard deviation', 'Cross Correlation'])
plotOptions = np.array(['Contour', 'Surface'])
pd.options.display.float_format = '{:.2E}'.format
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
            filename = input('Please enter a correct filename for the data turbine_32x32x8192.bin\n or press "q" to escape: ')
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
                    data = []
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

        # Get type of inputting
        print('\nHow do you want to do this?')
        input_selection = displayMenu(['Input a range of y and z values', 'Input specific points'])

        if input_selection == 1:
            # Get the desired y and z value
            ymin = get_int_in_range('Please enter a value for Ymin: ', 1, ranges[1])
            ymax = get_int_in_range('Please enter a value for Ymax: ', ymin, ranges[1])
            zmin = get_int_in_range('Please enter a value for Zmin: ', 1, ranges[2])
            zmax = get_int_in_range('Please enter a value for Zmax: ', zmin, ranges[2])
        elif input_selection == 2:
            n_points = get_int_in_range('Please enter number of points: ', 1, 100)
            points = np.zeros((n_points, 2), dtype=int)
            for i in range(n_points):
                points[i,0] = get_int_in_range('Please enter a value for y_{}: '.format(i+1), 1, ranges[1])
                points[i,1] = get_int_in_range('Please enter a value for z_{}: '.format(i+1), 1, ranges[2])

        if statistic in ['Mean', 'Variance', 'Standard deviation']:
            # Calculate the statistic
            Myz = dataStatistics(data, statistic)

            # Print to the user
            if input_selection == 1:
                
                df = pd.DataFrame(data=Myz[(ymin - 1):ymax, (zmin - 1):zmax])
                df.index = np.arange(ymin, ymax+1)
                df.columns = np.arange(zmin, zmax+1)
                
                print('\nThe {} of the data for the given ranges are below. Rows are y-values and Columns are z-values.\n'.format(statistic))
                print(df.to_string())
                
            elif input_selection == 2:
                for i in range(n_points):
                    print('The {} of the data, where y = {} and z = {}: {:.2E}'.format(statistic, points[i,0], points[i,1], Myz[points[i,0]-1, points[i,1]-1]))




        elif statistic == 'Cross Correlation':
            # Inquire about additional information
            yref = get_int_in_range('Please enter a value for Yref: ', 1, ranges[1])
            zref = get_int_in_range('Please enter a value for Zref: ', 1, ranges[2])
            DeltaX = get_int_in_range('Please enter a value for DeltaX: ', 1, ranges[0]-1)

            # Calculate the statistic
            Myz = dataStatistics(data, statistic, yref, zref, DeltaX)

            # Print to the user
            if input_selection == 1:
                df = pd.DataFrame(data=Myz[(ymin - 1):ymax, (zmin - 1):zmax])
                df.index = np.arange(ymin, ymax+1)
                df.columns = np.arange(zmin, zmax+1)
                print('\nThe {} of the data for the given ranges are below. Rows are y-values and Columns are z-values.\n'.format(statistic))
                print(df.to_string())
                
            elif input_selection == 2:
                for i in range(n_points):
                    print('The {} of the data, where y = {} and z = {}, \n Yref = {}, Zref = {} and DeltaX = {} : {:.3E}'.format(statistic, points[i,0], points[i,1], yref, zref, DeltaX, Myz[points[i,0]-1, points[i,1]-1]))




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
