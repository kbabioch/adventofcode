#! /usr/bin/env python3

def is_invalid_id(n):
    s = str(n)

    if len(s) % 2 != 0:
        return False
    
    half = len(s) // 2
    left, right = s[:half], s[half:]
    return left == right

# part 1
with open('input/day2') as f:

    total = 0

    for line in f:

        line = line.strip()

        if not line:
            continue

        ranges = line.split(',')

        for r in ranges:
            start, stop = r.split('-')
            start, stop = int(start), int(stop)

            for n in range(start, stop + 1):
                if is_invalid_id(n):
                    total += n

    print(total)

def is_invalid_id2(n):
    s = str(n)
    return s in (s + s)[1:-1]

# part 2
with open('input/day2') as f:

    total = 0

    for line in f:

        line = line.strip()

        if not line:
            continue

        ranges = line.split(',')

        for r in ranges:
            start, stop = r.split('-')
            start, stop = int(start), int(stop)

            for n in range(start, stop + 1):
                if is_invalid_id2(n):
                    total += n

    print(total)
