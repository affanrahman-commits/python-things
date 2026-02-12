num = input()
arr = []
for i in num:
    if int(i) == 4 or int(i) == 7:
        arr.append(i)
if len(arr) == 4 or len(arr) == 7:
    print("YES")
else:
    print("NO")