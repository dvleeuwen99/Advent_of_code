import re
import itertools

with open('input.txt') as input:
    input = [list(k) for k in [c.strip('\n') for c in input]]
input.append([])

total1 = 0
count = 0
answers = dict()
while len(input) >= 1:
    for idx, line in enumerate(input):
        if line == []:
            end = idx
            break
    reflections = []
    current_row = ''
    for idx, line in enumerate(input[:end]):
        if current_row == line:
            reflections.append([idx - 1, idx])
        current_row = line
    # print(reflections)
    answer = 0
    while len(reflections) >= 1:
        good = True
        start, finish = reflections[0]
        while good:
            if start > 0 and finish < end - 1:
                start -= 1
                finish += 1
            else:
                answer = 100 * reflections[0][1]
                good = False
            
            if input[start] != input[finish]:
                good = False
            # print(start, finish, good)
        reflections = reflections[1:]
    # print(answer)
    total1 += answer
    answers[count] = answer

    if answer == 0:     #try other reflection
        length = len(input[0])
        current_input = []
        for i in range(length):
            line = ''
            for j in range(end):
                line += input[j][i]
            current_input.append(line)
        reflections = []
        current_row = ''
        for idx, line in enumerate(current_input):
            if current_row == line:
                reflections.append([idx - 1, idx])
            current_row = line
        # print(reflections)
        answer = 0
        while len(reflections) >= 1:
            good = True
            start, finish = reflections[0]
            while good:
                if start > 0 and finish < len(current_input) - 1:
                    start -= 1
                    finish += 1
                else:
                    answer = reflections[0][1]
                    good = False
                
                if current_input[start] != current_input[finish]:
                    good = False
            reflections = reflections[1:]
        total1 += answer
        answers[count] = answer
        

    input = input[(end+1):]
    count += 1

print('res', total1)
print(answers)

with open('input.txt') as input:
    input = [list(k) for k in [c.strip('\n') for c in input]]
input.append([])

total2 = 0
count = 0
while len(input) >= 1:
    for idx, line in enumerate(input):
        if line == []:
            end = idx
            break
    current_input = input[:end]
    answer = 0
    found = False
    while found == False:
        for i, line in enumerate(current_input):
            if answer != 0 and answer != answers[count]:
                found = True
                break
            for j in range(len(current_input[0])):
                if current_input[i][j] == '#':
                    current_input[i][j] = '.'
                else:
                    current_input[i][j] = '#'
                # print('i', i, j, current_input[i], count)
                current_row = ''
                reflections = []
                for idx, line in enumerate(current_input):
                    if current_row == line:
                        reflections.append([idx - 1, idx])
                    current_row = line
                # print('row', reflections)
                answer = 0
                while len(reflections) >= 1:
                    good = True
                    start, finish = reflections[0]
                    while good:
                        if start > 0 and finish < end - 1:
                            start -= 1
                            finish += 1
                        else:
                            answer = 100 * reflections[0][1]
                            good = False
                        if current_input[start] != current_input[finish]:
                            good = False
                    if answer != answers[count] and answer != 0:
                        print('ans1', answer, count)
                        print('reflection', reflections[0],'row')
                        total2 += answer
                        found = True
                        break
                    reflections = reflections[1:]
                    if found == True:
                        break

                if answer == 0 or answer == answers[count]:     #try other reflection
                    length = len(input[0])
                    other_input = []
                    for k in range(length):
                        line = ''
                        for l in range(end):
                            line += current_input[l][k]
                        other_input.append(line)
                    reflections = []
                    current_row = ''
                    for idx, line in enumerate(other_input):
                        if current_row == line:
                            reflections.append([idx - 1, idx])
                        current_row = line
                    # print('column', reflections)
                    while len(reflections) >= 1:
                        good = True
                        start, finish = reflections[0]
                        while good:
                            if start > 0 and finish < len(other_input) - 1:
                                start -= 1
                                finish += 1
                            else:
                                answer = reflections[0][1]
                                good = False
                            
                            if other_input[start] != other_input[finish]:
                                good = False

                        if answer != answers[count] and answer != 0:
                            print('ans2', answer, count)
                            print('reflection', reflections[0], 'column')
                            total2 += answer
                            found = True
                            break
                        reflections = reflections[1:]
                        if found == True:
                            break
                if found == True:
                    break
                if current_input[i][j] == '#':
                    current_input[i][j] = '.'
                else:
                    current_input[i][j] = '#'               

    input = input[(end+1):]
    count += 1

print('res2', total2)









    
