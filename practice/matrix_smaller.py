rows = []
for i in range(4):
    row = list(map(int, input().split(" ")))
    if 1 in row:
        print(abs(i - 2) + abs(row.index(1) - 2))
        break