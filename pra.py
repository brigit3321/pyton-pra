# 素数を出力する関数

def prime_numbers(d):

    numbers = []

    for i in range(2, d + 1):
        flag = True
        for j in range(2, i):
            if i % j == 0:
                flag = False
                break
            
        if flag == True:
            numbers.append(i)

    return numbers

numbers = prime_numbers(10)
print(numbers)

# 約数

a, b, c = map(int, input().split())
count = 0

for i in range(a, b + 1):
    if c % i == 0:
        count += 1

print(count)
