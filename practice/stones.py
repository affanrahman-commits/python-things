number = int(input())
string = input()
counter = 0
i = 0
while i < number-1:
    if string[i] == string[i+1]:
        counter += 1
    i += 1
print(counter)