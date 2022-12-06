import collections

def checkStream(buffer):
    seen = set()
    return not any(i in seen or seen.add(i) for i in buffer)

buffer = collections.deque(maxlen=14)

with open('input.txt') as stream:
    unique = ''
    dataStream = stream.readline()
    total = 0 
    for char in dataStream:
        buffer.append(char)
        total += 1
        if total > 13:
            unique = checkStream(buffer)
        
        if unique is True:
            print('Done')
            print(f'Total Is: {total }')
            break
            

        