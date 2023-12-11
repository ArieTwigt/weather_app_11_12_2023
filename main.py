from custom_modules.calculation_functions import calc_circle
import argparse


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


# parse the arguments
args = parser.parse_args()

if __name__ == '__main__':
    my_diameter = args.diameter
    my_rounding = args.rounding
    
    my_circle = calc_circle(my_diameter, rounding=my_rounding)
    
    print(my_circle)
