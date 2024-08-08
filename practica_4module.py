nums = [6,7,4,2,1,8,10,3,5,9] # пузырьковая сортировка
def booble_sort(ls):
    snapped = True
    while snapped:
        snapped =False
        for i in range(len(ls) - 1):
            if ls[i] > ls[i+1]:
                ls[i],ls[i+1] = ls[i+1],ls[i]
                snapped = True


booble_sort(nums)
print(nums)

def selecion_sort(ls): # сортировка выбором
    for i in range(len(ls)):
        lowest = i
        for j in range(i+1,len(ls)):
            if ls[j] < ls[lowest]:
                lowest = j
        ls[i],ls[lowest] = ls[lowest],ls[i]


selecion_sort(nums)
print(nums)


def insersion_sort(ls):
    for i in range(1,len(ls)):
        key = ls[i]
        j = i - 1
        while ls[j+1] > key and j>=0:
            ls[j+1] = ls[j]
            j -=1
        ls[j+1] = key
    return ls

insersion_sort(nums)
print(nums)