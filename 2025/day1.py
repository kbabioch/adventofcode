start = 50

# part 1
with open('input/day1') as f:

    position = start
    zeroes = 0

    for line in f:

        line = line.strip()

        if not line:
            continue
        
        d, v = line[0], int(line[1:])
        position += v if d == 'R' else -v
        position %= 100

        zeroes += position == 0

print(f'zeroes: {zeroes}')

# part 2
with open('input/day1') as f:

    position = start
    zero_passes = 0

    for line in f:

        line = line.strip()

        if not line:
            continue
        
        d, v = line[0], int(line[1:])

        for _ in range(v):

            position += 1 if d == 'R' else -1
            position %= 100
            zero_passes += position == 0

print(f'zero_passes: {zero_passes}')
