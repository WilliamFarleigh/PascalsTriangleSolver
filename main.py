from PascalsTriangleSolver import *

# rEcUrSiOn Is NoT pYtHoNiC
def get_input_size_of_binomial() -> int:
    while True:
        try:
            return int(input("Which line would you like to calculate? "))
        except:
            print("That is not a valid integer!")

print(get_pascals_triangle_line(get_input_size_of_binomial()))