def get_fib(position):
    if position == 0: return 0
    if position == 1: return 1
    sequence = [0, 1]
    for i in range(position+1):
        p1 = sequence[i]
        p2 = sequence[i+1]
        sequence.append(p1+p2)
    return sequence[position]

print(get_fib(0))
print(get_fib(5))
print(get_fib(9))
