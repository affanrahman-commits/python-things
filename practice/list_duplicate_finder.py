numbers = []
while True:
    value = input("Enter numbers: ")
    try:
        int_value = int(value)
        numbers.append(int_value)
    except ValueError:
        if value == "quit":
            break
        else:
            print("Unknown command!")
new_list = []
for number in numbers:
    if number not in new_list:
        new_list.append(number)
print(new_list)