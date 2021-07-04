def recursive(num):
    if num <= 0:
        return num
    else:
        print('call')
        output = recursive(num-1)
        return output

print(recursive(3))
