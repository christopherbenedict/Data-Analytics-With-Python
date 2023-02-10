"""
This file utilizes the cover dataset (https://archive.ics.uci.edu/ml/datasets/Covertype) for class AFS 505 Spring 2023. 
Author: Chris Benedict

This file can be used by anyone, assuming it works, please enjoy yourself.
   
"""
#Checkoff
#1.) arguments passed via the command-line CHECK
#2.) use of lists or dictionaries CHECK
#3.) use of functions CHECK
#4.) use of loops CHECK
#5.) proper commenting CHECK

from sys import argv

import pprint
pp = pprint.PrettyPrinter(indent=4)

#Set global variables
AREAS = {
    0: 'All',
    1: 'Rawah Wilderness Area',
    2: 'Neota Wilderness Area',
    3: 'Comanche Peak Wilderness Area',
    4: 'Cache la Poudre Wilderness Area'
}

COLUMNS = {
    0: 'Elevation',
    1: 'Aspect',
    2: 'Slope',
    3: 'Horizontal_Distance_To_Hydrology',
    4: 'Vertical_Distance_To_Hydrology',
    5: 'Horizontal_Distance_To_Roadways',
    6: 'Hillshade_9am',
    7: 'Hillshade_Noon',
    8: 'Hillshade_3pm',
    9: 'Horizontal_Distance_To_Fire_Points'
}

def main():
    """
    Reads in dataset and assigns dictionary

    """
    print("File has been run")
    #1.) Read the covtype.data
    #Bring in file and prepare for loop
    cover = open('covtype.data', 'r')
    line1 = cover.readline()
    line2 = cover.readline()
   
    #Create dictionaries
    elevation_sum = 0
    elevation_min = float('inf')
    elevation_max = 0
    aspect_sum = 0
    aspect_min = float('inf')
    aspect_max = 0
    slope_sum = 0
    slope_min = float('inf')
    slope_max = 0
    horizontal_distance_to_hydrology_sum = 0
    horizontal_distance_to_hydrology_min = float('inf')
    horizontal_distance_to_hydrology_max = 0
    vertical_distance_to_hydrology_sum = 0
    vertical_distance_to_hydrology_min = float('inf')
    vertical_distance_to_hydrology_max = 0
    horizontal_distance_to_roadways_sum = 0
    horizontal_distance_to_roadways_min = float('inf')
    horizontal_distance_to_roadways_max = 0
    hillshade_9am_sum = 0
    hillshade_9am_min = float('inf')
    hillshade_9am_max = 0
    hillshade_noon_sum = 0
    hillshade_noon_min = float('inf')
    hillshade_noon_max = 0
    hillshade_3pm_sum = 0
    hillshade_3pm_min = float('inf')
    hillshade_3pm_max = 0
    horizontal_distance_to_fire_points_sum = 0
    horizontal_distance_to_fire_points_min = float('inf')
    horizontal_distance_to_fire_points_max = 0
    num_lines = 0
    
 
    

    #Split at commas and calculate values.
    for data in cover:
        cols = data.strip().split(',')
        num_lines = num_lines + 1
        elevation = float(cols[0])
        elevation_sum = elevation_sum + elevation
        elevation_min = min([elevation, elevation_min])
        elevation_max = max([elevation, elevation_max])
        elevation_mean = round((elevation_sum/num_lines),2)
        aspect = float(cols[1])
        aspect_sum = aspect_sum + aspect
        aspect_min = min([aspect, aspect_min])
        aspect_max = max([aspect, aspect_max])
        aspect_mean = round((aspect_sum/num_lines),2)
        slope = float(cols[2])
        slope_sum = slope_sum + slope
        slope_min = min([slope, slope_min])
        slope_max = max([slope, slope_max])
        slope_mean = round((slope_sum/num_lines),2)
        horizontal_distance_to_hydrology = float(cols[3])
        horizontal_distance_to_hydrology_sum = horizontal_distance_to_hydrology_sum + horizontal_distance_to_hydrology
        horizontal_distance_to_hydrology_min = min([horizontal_distance_to_hydrology, horizontal_distance_to_hydrology_min])
        horizontal_distance_to_hydrology_max = max([horizontal_distance_to_hydrology, horizontal_distance_to_hydrology_max])
        horizontal_distance_to_hydrology_mean = round((horizontal_distance_to_hydrology_sum/num_lines),2)
        vertical_distance_to_hydrology = float(cols[4])
        vertical_distance_to_hydrology_sum = vertical_distance_to_hydrology_sum + vertical_distance_to_hydrology
        vertical_distance_to_hydrology_min = min([vertical_distance_to_hydrology, vertical_distance_to_hydrology_min])
        vertical_distance_to_hydrology_max = max([vertical_distance_to_hydrology, vertical_distance_to_hydrology_max])
        vertical_distance_to_hydrology_mean = round((vertical_distance_to_hydrology_sum/num_lines),2)
        horizontal_distance_to_roadways = float(cols[5])
        horizontal_distance_to_roadways_sum = horizontal_distance_to_roadways_sum + horizontal_distance_to_roadways
        horizontal_distance_to_roadways_min = min([horizontal_distance_to_roadways, horizontal_distance_to_roadways_min])
        horizontal_distance_to_roadways_max = max([horizontal_distance_to_roadways, horizontal_distance_to_roadways_max])
        horizontal_distance_to_roadways_mean = round((horizontal_distance_to_roadways_sum/num_lines),2)
        hillshade_9am = float(cols[6])
        hillshade_9am_sum = hillshade_9am_sum + hillshade_9am
        hillshade_9am_min = min([hillshade_9am_sum, hillshade_9am_min])
        hillshade_9am_max = max([hillshade_9am_sum, hillshade_9am_max])
        hillshade_9am_mean = round((hillshade_9am_sum/num_lines),2)
        hillshade_noon = float(cols[7])
        hillshade_noon_sum = hillshade_noon_sum + hillshade_noon
        hillshade_noon_min = min([hillshade_noon, hillshade_noon_min])
        hillshade_noon_max = max([hillshade_noon, hillshade_noon_max])
        hillshade_noon_mean = round((hillshade_noon_sum/num_lines),2)
        hillshade_3pm = float(cols[8])
        hillshade_3pm_sum = hillshade_3pm_sum + hillshade_3pm
        hillshade_3pm_min = min([hillshade_3pm_sum, hillshade_3pm_min])
        hillshade_3pm_max = max([hillshade_3pm, hillshade_3pm_max])
        hillshade_3pm_mean = round((hillshade_3pm_sum/num_lines),2)
        horizontal_distance_to_fire_points = float(cols[9])
        horizontal_distance_to_fire_points_sum = horizontal_distance_to_fire_points_sum + horizontal_distance_to_fire_points
        horizontal_distance_to_fire_points_min = min([horizontal_distance_to_fire_points, horizontal_distance_to_fire_points_min])
        horizontal_distance_to_fire_points_max = max([horizontal_distance_to_fire_points, horizontal_distance_to_fire_points_max])
        horizontal_distance_to_fire_points_mean = round((horizontal_distance_to_fire_points_sum/num_lines),2)
    print(elevation_mean, elevation_min) 
    print(elevation_min)
    print(elevation_max)
    print(aspect_mean)
    print(aspect_min)
    print(aspect_max)
    print(slope_mean)
    print(slope_min)
    print(slope_max)
    print(horizontal_distance_to_hydrology_mean)
    print(horizontal_distance_to_hydrology_min)
    print(horizontal_distance_to_hydrology_max)
    print(vertical_distance_to_hydrology_mean)
    print(vertical_distance_to_hydrology_min)
    print(vertical_distance_to_hydrology_max)
    print(horizontal_distance_to_roadways_mean)
    print(horizontal_distance_to_roadways_min)
    print(horizontal_distance_to_roadways_max)
    print(hillshade_9am_mean)
    print(hillshade_9am_min)
    print(hillshade_9am_max)
    print(hillshade_noon_mean)
    print(hillshade_noon_min)
    print(hillshade_noon_max)
    print(hillshade_3pm_mean)
    print(hillshade_3pm_min)
    print(hillshade_3pm_max)
    print(horizontal_distance_to_fire_points_mean)
    print(horizontal_distance_to_fire_points_min)
    print(horizontal_distance_to_fire_points_max)
    
    # Close the file and print the results.
    cover.close()
    
    #Create new file to add output from above to.
    output_file = open("p01_output.txt", "w")
    print_column_stats(output_file, COLUMNS[0], elevation_min, elevation_max, elevation_mean)
    print_column_stats(output_file, COLUMNS[1], aspect_min, aspect_max, aspect_mean)
    print_column_stats(output_file, COLUMNS[2], slope_min, slope_max, slope_mean)
    print_column_stats(output_file, COLUMNS[3], horizontal_distance_to_hydrology_min, horizontal_distance_to_hydrology_max, horizontal_distance_to_hydrology_mean)
    print_column_stats(output_file, COLUMNS[4], vertical_distance_to_hydrology_min, vertical_distance_to_hydrology_max, vertical_distance_to_hydrology_mean)
    print_column_stats(output_file, COLUMNS[5], horizontal_distance_to_roadways_min, horizontal_distance_to_roadways_max, horizontal_distance_to_roadways_mean)
    print_column_stats(output_file, COLUMNS[6],  hillshade_9am_min,  hillshade_9am_max,  hillshade_9am_mean)
    print_column_stats(output_file, COLUMNS[7], hillshade_noon_min, hillshade_noon_max, hillshade_noon_mean)
    print_column_stats(output_file, COLUMNS[8],  hillshade_3pm_min,  hillshade_3pm_max,  hillshade_3pm_mean)
    print_column_stats(output_file, COLUMNS[9], horizontal_distance_to_fire_points_min, horizontal_distance_to_fire_points_max, horizontal_distance_to_fire_points_mean)
    
    # Close the file.
    output_file.close()             

def print_column_stats (output_file, columnname, minvalue, maxvalue, meanvalue):
    output_file.write("{}, the Minimum value is {}, the Maximum value is {} and the Average value is {}\n".format(columnname, minvalue, maxvalue, meanvalue))
    
if __name__== "__main__" :
    main()