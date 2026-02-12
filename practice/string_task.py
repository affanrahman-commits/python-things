string = input().lower()
array = []
output = ""
for ch in string:
    if ch == "a":
        continue
    elif ch == "e":
        continue
    elif ch == "i":
        continue
    elif ch == "o":
        continue
    elif ch == "u":
        continue
    elif ch == "y":
        continue
    else:
        array.append(ch)
for _ in array:
    output += "." + _
print(output)