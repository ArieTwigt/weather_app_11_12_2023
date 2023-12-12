from custom_modules.calculation_functions import calc_circle
import argparse

float()
int()
str()
[]

# initate a argument parser instance
parser = argparse.ArgumentParser()

# add arguments to the parser
parser.add_argument("--diameter", "-d", 
                    type=float, 
                    required=True, 
                    help="Required: The diameter of the circle")

parser.add_argument("--rounding", "-r", 
                    type=int, 
                    required=False, 
                    default=1, 
                    help="Optional: Rounding for the value")

parser.add_argument("--export_type", "-e",
                    type=str,
                    required=False,
                    choices=['csv', 'print'],
                    default='print')


parser.add_argument("--diameters_list", "-dl",
                    required=False,
                    type=lambda s: [int(item) for item in s.split(',')])


# parse the arguments
args = parser.parse_args()

if __name__ == '__main__':
    my_diameter = args.diameter
    my_rounding = args.rounding
    export_type = args.export_type
    my_diameters_list = args.diameters_list
    
    my_circle = calc_circle(my_diameter, rounding=my_rounding)
    
    # output based on the export type
    if export_type == 'csv':
        print("Exporting to csv")
    else:
        print(my_diameters_list)
        print(my_circle)
