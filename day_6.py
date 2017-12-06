import copy

banks = list(map(int, '0	5	10	0	11	14	13	4	11	8	8	7	1	4	12	11'.split()))
# banks = list(map(int, '0	2	7	0	'.split()))


history = list()
history.append(copy.copy(banks))
counter = 0
loop = True

while loop:
    counter += 1
    max_index = banks.index(max(banks))
    max_num = max(banks)
    banks[max_index] = 0
    for i in range(1, max_num+1):
        if max_index<len(banks)-1:
            max_index += 1
        else:
            max_index = 0
        banks[max_index] += 1
    for i in history:
        if banks == i:
            loop = False
    history.append(copy.copy(banks))

print(counter)
last = copy.copy(banks)

loop = True
counter = 0
while loop:
    counter += 1
    max_index = banks.index(max(banks))
    max_num = max(banks)
    banks[max_index] = 0
    for i in range(1, max_num+1):
        if max_index<len(banks)-1:
            max_index += 1
        else:
            max_index = 0
        banks[max_index] += 1
    for i in history:
        if banks == last:
            loop = False

print(counter)
