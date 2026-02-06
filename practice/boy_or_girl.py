word = input("")
letter_list = []
for i in word:
    if i not in letter_list:
        letter_list.append(i)
if len(letter_list) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")