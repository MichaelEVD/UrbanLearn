def is_prime(func):
    def simp_or_comp(*args):
        a = func(*args)
        if a % 2 == 0 :
            print('Составное')
        else:
            print('Простое')
        return a
    return simp_or_comp
@is_prime
def sum_three(*args):
    sum_numb = sum(args)
    return sum_numb


result = sum_three(2, 3, 6)
print(result)


