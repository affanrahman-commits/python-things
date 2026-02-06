n = int(input(""))
placeholder = 0
for i in range(n):
    statement = input("")
    if statement == "X++":
        placeholder += 1
    elif statement == "++X":
        placeholder += 1
    elif statement == "X--":
        placeholder -= 1
    elif statement == "--X":
        placeholder -= 1
print(placeholder)