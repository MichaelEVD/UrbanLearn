n = int(input("введите целое число от 3 до 20 "))
list = []
for i in range(1,n) :
     for j in range(i + 1,n) :
        sum = i + j
        if n % sum == 0 :
            list.append(i)
            list.append(j)
print(*list, sep = '')

