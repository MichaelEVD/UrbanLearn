
def is_prime(func):
    def wrapper(*args):
        a = func(*args)
        flag = 0
        for i in range(2,a):
            if a % i == 0:
                flag += 1
        if flag == 0:
            print('Простое')
        else:
            print('Составное')
        return a
    return wrapper
@is_prime
def sum_three(*args):
    sum_numb = sum(args)
    return sum_numb


result = sum_three(2, 3, 6)
print(result)


