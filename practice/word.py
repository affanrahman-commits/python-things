word = input()
lower_letters = []
upper_letters = []
for ch in word:
    if ch.islower():
        lower_letters.append(ch)
    else:
        upper_letters.append(ch)
if len(lower_letters) >= len(upper_letters):
    print(word.lower())
else:
    print(word.upper())