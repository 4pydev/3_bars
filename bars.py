import json
import sys
from math import sqrt


def load_data(filepath):
    with open(filepath) as init_file:
        return json.load(init_file)


def get_biggest_bar(bars_data_dict):
    max_bar = max([bar['properties']['Attributes']['SeatsCount']
         for bar in bars_data_dict['features']])
    max_bar_name = ''
    for bar in bars_data_dict['features']:
        if bar['properties']['Attributes']['SeatsCount'] == max_bar:
            max_bar_name = bar['properties']['Attributes']['Name']
    return max_bar_name

def get_smallest_bar(bars_data_dict):
    min_bar = min([bar['properties']['Attributes']['SeatsCount']
                   for bar in bars_data_dict['features']])
    min_bar_name = ''
    for bar in bars_data_dict['features']:
        if bar['properties']['Attributes']['SeatsCount'] == min_bar:
            min_bar_name = bar['properties']['Attributes']['Name']
    return min_bar_name

def get_dist_to_bar(usr_long, usr_lat, bar_long, bar_lat):
    return sqrt((usr_long - bar_long)**2 + (usr_lat - bar_lat)**2)


def get_closest_bar(bars_data_dict, user_longitude, user_latitude):
    min_dist_to_bar = 2000000000.0
    closest_bar_name = ''
    for bar in bars_data_dict['features']:
        bar_longitude, bar_latitude = bar['geometry']['coordinates']
        dist_to_bar = get_dist_to_bar(user_longitude, user_latitude,
                                          bar_longitude, bar_latitude)
        if dist_to_bar < min_dist_to_bar:
            min_dist_to_bar = dist_to_bar
            closest_bar_name = bar['properties']['Attributes']['Name']
    return closest_bar_name




if __name__ == '__main__':
    try:
        path_to_file = sys.argv[1]
        init_data_dict = load_data(path_to_file)

        print("The biggest bar is: {}".
              format(get_biggest_bar(init_data_dict)))
        print("The smallest bar is: {}".
              format(get_smallest_bar(init_data_dict)))
        print("--------------------------------------")

        user_longitude = float(input("Enter your longitude: "))
        user_latitude = float(input("Enter your latitude: "))
        print("{} is closest bar to you.".format(get_closest_bar(
            init_data_dict, user_longitude, user_latitude)))

    except IndexError as index_error:
        print("You must enter a path to data file.")
    except OSError as file_not_found_error:
        print("{} - File not found.".format(sys.argv[1]))
