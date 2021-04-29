#素数を出力する関数

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