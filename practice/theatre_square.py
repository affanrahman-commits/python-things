import math
numbers = input("")
numbers_list_str = numbers.split(" ")
numbers_list = map(int, numbers_list_str)
x,y,z = numbers_list
tiles_along_length = math.ceil(x/z)
tiles_along_width = math.ceil(y/z)
total_tiles = tiles_along_length * tiles_along_width
print(total_tiles)