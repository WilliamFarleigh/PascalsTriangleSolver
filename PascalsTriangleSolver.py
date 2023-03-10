import math
def get_pascals_triangle_line(lineAsNumber : int, *args, **kwargs) -> str:
    line = ""
    for r in range(lineAsNumber + 1):
        line = line + " " + str(int(math.factorial(lineAsNumber)/(math.factorial(lineAsNumber - r) * math.factorial(r))))
    return line