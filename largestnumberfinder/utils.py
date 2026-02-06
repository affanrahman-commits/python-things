def list_maker(value):
    value_list = value.split(" ")
    return value_list
def find_max(values):
    largest = values[0]
    for value in values:
        if value > largest:
            largest = value
    return largest