input = []

import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'test1.txt')

with open(file_path, 'r') as file:
    for line in file:
        # process each line
        input.append((line.strip()))

# print(input)

total1 = 0
for i in input:
    before, after = i.split(':')
    after = [*map(int, after.split(' ')[1:])]
    # print(before)
    # print(after)
    before = int(before)
    options = set()
    for a in range(len(after)):
        # print(a)
        new = after[a]
        if len(options) == 0:
            options.add(new)
        else:
            newoptions = set()
            for o in options:
                add = o + new
                mul = o * new
                if add <= before:
                    newoptions.add(add)
                if mul <= before:
                    newoptions.add(mul)
                con = int(str(o) + str(new))
                # print(o, new, con)
                if con <= before:
                    newoptions.add(con)
                # print(newoptions)
                options = newoptions
        # print(options)
    if before in options:
        total1 += before
        # print(before)

        
print(total1)
                
            




        

