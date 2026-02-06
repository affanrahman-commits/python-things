n = int(input(""))
counter = 0
for i in range(n):
    second_counter = 0
    solvers = input("")
    list_solvers = solvers.split(" ")
    for values in list_solvers:
        if int(values) == 1:
            second_counter += 1
    if second_counter >= 2:
        counter += 1
print(counter)