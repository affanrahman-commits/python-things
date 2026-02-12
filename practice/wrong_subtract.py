n, k = input().split(" ")
k = int(k)
for i in range(k):
    if n[-1] == "0":
        n = int(n)
        n //= 10
        n = str(n) 
    elif n[-1] != 0:
        n = int(n)
        n -= 1   
        n = str(n)
print(n)