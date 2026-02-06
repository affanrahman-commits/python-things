n = int(input(""))
words = input("")
words_list = words.split(" ")
if len(words_list) == n:
    for word in words_list:
        if len(word) > 10:
            first_letter = word[0]
            last_letter = word[-1]
            middle_letters = len(word[1:-1])
            print(f"{first_letter}{middle_letters}{last_letter}")
        else:
            print(word)
else:
    print("Invalid inputs!")
    quit