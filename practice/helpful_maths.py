numbers_list = list(map(int, input("").split("+")))
temp_list = []
temp_output = ""
j = 0
looper = len(numbers_list)
while j < looper:
    smallest_number = numbers_list[0]
    for i in numbers_list:
        if i < smallest_number:
            smallest_number = i
    temp_list.append(smallest_number)
    numbers_list.remove(smallest_number)
    j += 1
for i in temp_list:
    temp_output += f"{i}+"
output = temp_output[0:-1]
print(output)