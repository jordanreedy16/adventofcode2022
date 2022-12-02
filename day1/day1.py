array = []
elfCals = 0

def find_three_largest(arr):
    result = [None]*3
    for val in arr:
        update_result(result, val)
    return result

def update_result(result, val):
    if result[2] is None or val > result[2]:
        update_and_shift(result, val, 2)
    elif result[1] is None or val > result[1]:
        update_and_shift(result, val, 1)
    elif result[0] is None or val > result[0]:
        update_and_shift(result, val, 0)

def update_and_shift(result, val, idx):
    for i in range(idx+1):
        if i == idx:
            result[i] = val
        else:
            result[i] = result[i+1]

with open('input.txt') as cal_file:
    for line in cal_file:
        if line != '\n':
            elfCals = int(line) + elfCals
        elif line == '\n':
            array.append(elfCals)
            elfCals = 0
            continue

print(max(array))



# For finding top 3
#top3 = find_three_largest(array)
#print(top3)

#print(sum(top3))