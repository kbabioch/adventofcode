#! /usr/bin/env python3

# part 1
with open('input/day3') as f:
    total_sum = 0
    
    for line in f:
        line = line.strip()
        bank_max = 0
        
        for i in range(len(line)):
            for j in range(i + 1, len(line)):
                tens = line[i]
                ones = line[j]
                joltage = int(tens + ones)
                
                if joltage > bank_max:
                    bank_max = joltage
        
        total_sum += bank_max

    print(total_sum)

# part 2
with open('input/day3') as f:
    total_sum = 0
    needed_length = 12

    for line in f:
        line = line.strip()
        
        if len(line) < needed_length:
            continue

        index = 0
        digits = []
        
        for i in range(needed_length):
            must_keep = (needed_length - 1) - i
            search_end = len(line) - must_keep
            window = line[index : search_end]
            max_digit = max(window)
            local_index = window.find(max_digit)
            digits.append(max_digit)
            index = index + local_index + 1
        
        bank_value = int("".join(digits))
        total_sum += bank_value

    print(total_sum)
