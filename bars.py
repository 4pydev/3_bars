import json
import sys
from math import sqrt


def load_data(filepath):
    with open(filepath) as init_file:
        return json.load(init_file)


def get_biggest_bar(bars_list):
    return max(bars_list, key=lambda bar:
               bar['properties']['Attributes']['SeatsCount'])


def get_smallest_bar(bars_list):
    return min(bars_list, key=lambda bar:
               bar['properties']['Attributes']['SeatsCount'])


def get_closest_bar(bars_list, usr_lat, usr_lon):
    return min(bars_list, key=lambda bar: sqrt(
               (usr_lat-bar['geometry']['coordinates'][0])**2) +
               (usr_lon-bar['geometry']['coordinates'][1])**2)


def print_bar_info(bar, status):
    print("The {status} bar is \n\tName: {name} \n\tAddress: {address}"
          .format(name=bar['properties']['Attributes']['Name'],
                  address=bar['properties']['Attributes']['Address'],
                  status=status))


if __name__ == '__main__':
    try:
        path_to_file = sys.argv[1]
        bars_list = load_data(path_to_file)['features']

        biggest_bar = get_biggest_bar(bars_list)
        print_bar_info(biggest_bar, 'biggest')

        smallest_bar = get_smallest_bar(bars_list)
        print_bar_info(smallest_bar, 'smallest')

        print("------------------------------------------------")

        usr_lat = float(input("Enter your latitude: "))
        usr_lon = float(input("Enter your longitude: "))

        closest_bar = get_closest_bar(bars_list, usr_lat, usr_lon)
        print_bar_info(closest_bar, 'closest')

    except IndexError:
        print("You must enter a path to data file.")
    except OSError:
        print("{} - File not found.".format(sys.argv[1]))
    except ValueError:
        print("You must enter valid coordinates values.")
