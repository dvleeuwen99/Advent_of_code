import re
import itertools

with open('input.txt') as input:
    input = [c.strip('\n') for c in input]


# print(input)

modules = {'button': ['broadcaster']}
parents = {}
for line in input:
    option = ''
    first, second = line.split(' -> ')
    children = second.split(', ')
    if first[0] == '%' or first[0] == '&':
        option = first[0]
        rest = first[1:]
    print(first, children)
    if option == first[0]:
        modules[rest] = [option, children]
    else:
        modules[first] = [children]
    for child in children:
        if option == first[0]:
            if child in parents:
                parents[child].append(rest)
            else:
                parents[child] = [rest]
        else:
            if child in parents:
                parents[child].append(first)
            else:
                parents[child] = [first]

# print(modules)
# print(parents)
for parent in parents:
    if parent in modules:
        if modules[parent][0] == '%':
            modules[parent].append(['flip', {parents[parent][0]:[0]}, 0])
        elif modules[parent][0] == '&':
            if len(parents[parent]) == 1:
                modules[parent].append(['inv',{parents[parent][0]:[0]}])
            else:
                pa = len(parents[parent])
                pas = {}
                for p in range(pa):
                    pas[parents[parent][p]] = [0]
                modules[parent].append(['con', pas])
        else:
            modules[parent].append(['button', {parents[parent][0]:[0]}])

print(modules)
for module in modules.items():
    print(module)
#print('module', 'list:(type, children, type with parents, state)')
buttonPress = 0
count_high = 0
count_low = 0
count = 0
cycles = {'fh': None, 'fn': None, 'lk': None, 'hh': None} ## still hard-coded in

def press(dict,buttonPress, count_high, count_low, count):
    buttonPress += 1
    pulses = [['button', 0]]
    while len(pulses) >= 1:
        new_pulses = []
        current = pulses[0]
        button = current[0]
        pulse = current[1]
        if button == 'nc':  ## still hard-coded in
            parents = dict[button][2][1]
            for p in parents:
                if cycles[p] == None:
                    if dict[button][2][1][p] == [1]:
                        cycles[p] = buttonPress
        if button != 'button':
            if pulse == 0:
                count_low += 1
            else:
                count_high += 1
            count += 1
        pulses.remove(current)
        if len(dict[button]) > 2 :
            parents = dict[button][2][1:]
            option = dict[button][2][0]
            if option == 'flip':
                if pulse == 0:
                    state = parents[1]
                    if state == 0:
                        dict[button][2][2] = 1
                        for push in dict[button][1]:
                            if push in dict:
                                new_pulses.append([push, 1])
                                if dict[push][2][0] == 'inv' or dict[push][2][0] == 'con':
                                    dict[push][2][1][button] = [1]
                            else:
                                count_high += 1
                                count += 1
                            
                    elif state == 1:
                        dict[button][2][2] = 0
                        for push in dict[button][1]:
                            if push in dict:
                                new_pulses.append([push, 0])
                                if dict[push][2][0] == 'inv' or dict[push][2][0] == 'con':
                                    dict[push][2][1][button] = [0]
                            else:
                                count_low += 1
                                count += 1
                            
            elif option == 'inv':
                if pulse == 1:
                    for push in dict[button][1]:
                        if push in dict:
                            new_pulses.append([push, 0])
                            if dict[push][2][0] == 'inv' or dict[push][2][0] == 'con':
                                dict[push][2][1][button] = [0]
                        else:
                            count_low += 1
                            count += 1
            
                            
                else:
                    for push in dict[button][1]:
                        if push in dict:
                            new_pulses.append([push, 1])
                            if dict[push][2][0] == 'inv' or dict[push][2][0] == 'con':
                                dict[push][2][1][button] = [1]
                        else:
                            count_high += 1
                            count += 1
                            
            elif option == 'con':
                push_value = 0
                for parent in parents[0].keys():
                    if parents[0][parent] == [0]:
                        push_value = 1
                        break
                for push in dict[button][1]:
                    if push in dict:
                        new_pulses.append([push,push_value])
                        if dict[push][2][0] == 'inv' or dict[push][2][0] == 'con':
                            dict[push][2][1][button] = [1]
                    else:
                        if push_value == 0:
                            count_low += 1
                        else:
                            count_high += 1
                        count += 1
                
        else:
            if len(dict[button]) == 1 and isinstance(dict[button][0],str):
                new_pulses.append([dict[button][0], pulse])
            else:
                for push in dict[button][0]:
                    if push in dict:
                        new_pulses.append([push, pulse])
        for new in new_pulses:
            pulses.append(new)

    return dict, buttonPress, count_high, count_low, count

while buttonPress < 5000:
    if buttonPress == 1000:
        print('part1', count_high*count_low)
    modules, buttonPress, count_high, count_low, count = press(modules, buttonPress, count_high, count_low, count)

print(cycles)
total2 = 1
for cycle in cycles:
    total2 *= cycles[cycle]
print('part2', total2)











    
