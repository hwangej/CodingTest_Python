num = int(input())
number = num
cnt = 0

while True:
    a = num // 10
    b = num % 10
    c = (a + b) % 10
    num = (b * 10) + c

    cnt = cnt + 1
    if(number == num ):
        break

print(cnt)
