lines = int(input())
sum_x = 0
sum_y = 0
sum_z = 0
for i in range(lines):
    x,y,z = map(int, input().split(" "))
    sum_x += x
    sum_y += y
    sum_z += z
    x = 0
    y = 0
    z = 0
if sum_x == 0 and sum_y == 0 and sum_z == 0:
    print("YES")
else:
    print("NO")