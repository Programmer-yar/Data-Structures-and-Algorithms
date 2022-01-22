def recursive(num):
    if num <= 0:
        return num
    else:
        print('recursive call at: ', num)
        output = recursive(num-1)
        return output

print(recursive(3))
