n = int(input(""))
for i in range(n):
    word = input("")
    if len(word) > 10:
            first_letter = word[0]
            last_letter = word[-1]
            middle_letters = len(word[1:-1])
            print(f"{first_letter}{middle_letters}{last_letter}")
    else:
          print(word)        