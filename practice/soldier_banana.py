k,n,w = map(int, input().split(" "))
total_money = 0
for i in range(w):
    total_money += (i+1) * k
if total_money > n:
    print(total_money - n)
else:
    print(0)