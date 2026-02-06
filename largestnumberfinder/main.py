import utils
numbers = input("Enter numbers: ")
numbers_list = utils.list_maker(numbers)
maximum = utils.find_max(numbers_list)
print(maximum)