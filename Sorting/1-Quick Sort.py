a=[8, 3, 1, 7, 0, 10, 2]
p_index = len(a)-1
pivot = a[p_index]

def quick_sort(a):
    p_index = len(a)-1
    print(p_index)
    pivot = a[p_index]
    print(pivot)
    for i,n in enumerate(a):
        while pivot < a[i] and i < p_index:
            temp1 = a[p_index-1]
            print(temp1)
            a[p_index-1] = pivot
            a[p_index] = a[i]
            a[i] = temp1
            p_index = p_index-1
            print(a)
    return a

a1=quick_sort(a)
print(a1)
a2 = quick_sort(a1)
print(a2)


