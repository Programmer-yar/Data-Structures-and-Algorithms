def search(array, value):
    original_array = array[:]
    mid = round(len(array)/2) -1
    for i in range(mid):
        if value == array[mid]:
            print('value found')
            return mid
        elif value > array[mid]:
            array = array[mid+1:]
            print('right slice: ', array)
            mid = round(len(array)/2) - 1
        elif value < array[mid]:
            array = array[:mid]
            print('left slice: ', array)
            mid = round(len(array)/2) - 1

        if len(array) == 0:
            print('NOT Found')
            return -1
            break

print(search([1,3,9,11,15,19,29], 11))
print(search([1,3,9,11,15,19,29], 1))
