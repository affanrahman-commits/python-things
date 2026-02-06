second_movement_1 = 0
second_movement_2 = 0
second_movement_3 = 0
second_movement_4 = 0
second_movement_5 = 0
rows = []
for i in range(0,5):
    rows.append(list(map(int, input().split(" "))))

first_row = rows[0]
second_row = rows[1]
third_row = rows[2]
fourth_row = rows[3]
fifth_row = rows[4]

if 1 in rows[0]:
    index_1 = rows[0].index(1) + 1
    movement = abs(index_1 - 3)
    second_movement_1 = 1
if 1 in rows[1]:
    index_2 = rows[1].index(1) + 1
    movement = abs(index_2 - 3)
    second_movement_2 = 1
if 1 in rows[2]:
    index_3 = rows[2].index(1) + 1
    movement = abs(index_3 - 3)
    second_movement_3 = 1
if 1 in rows[3]:
    index_4 = rows[3].index(1) + 1
    movement = abs(index_4 - 3)
    second_movement_4 = 1
if 1 in rows[4]:
    index_5 = rows[4].index(1) + 1
    movement = abs(index_5 - 3)
    second_movement_5 = 1

if second_movement_1 == 1:
    print(movement + 2)
if second_movement_2 == 1:
    print(movement + 1)
if second_movement_3 == 1:
    print(movement)
if second_movement_4 == 1:
    print(movement + 1)
if second_movement_5 == 1:
    print(movement + 2)