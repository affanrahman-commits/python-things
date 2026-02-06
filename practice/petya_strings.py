first_word = input("").lower()
second_word = input("").lower()
if first_word > second_word:
    print(1)
elif second_word > first_word:
    print(-1)
else:
    print(0)