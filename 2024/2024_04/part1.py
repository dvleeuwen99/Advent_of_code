input = []

with open('input.txt', 'r') as file:
    for line in file:
        # process each line
        input.append((line.strip()))

# print(input)

words = 0
length = len(input)
for ix, line in enumerate(input):
    for jx, j in enumerate(line):
        # print(ix, jx, j)
        # print(input[ix][jx])
        if j == 'X':
            if ix+1 <= length - 3 and input[ix+1][jx] == 'M':
                if input[ix+2][jx] == 'A' and input[ix+3][jx] == 'S':
                    words += 1
            if ix-1 >= 2 and input[ix-1][jx] == 'M' :
                if input[ix-2][jx] == 'A' and input[ix-3][jx] == 'S':
                    words += 1
            if jx+1 <= length - 3 and input[ix][jx+1] == 'M':
                if input[ix][jx+2] == 'A' and input[ix][jx+3] == 'S':
                    words += 1
            if jx-1 >= 2 and input[ix][jx-1] == 'M':
                if input[ix][jx-2] == 'A' and input[ix][jx-3] == 'S':
                    words += 1
            if ix+1 <= length - 3 and jx+1 <= length - 3 and input[ix+1][jx+1] == 'M':
                if input[ix+2][jx+2] == 'A' and input[ix+3][jx+3] == 'S':
                    words += 1
            if ix-1 >= 2 and jx-1 >= 2 and input[ix-1][jx-1] == 'M':
                if input[ix-2][jx-2] == 'A' and input[ix-3][jx-3] == 'S':
                    words += 1
            if ix-1 >= 2 and jx+1 <= length - 3 and input[ix-1][jx+1] == 'M':
                if input[ix-2][jx+2] == 'A' and input[ix-3][jx+3] == 'S':
                    words += 1
            if ix+1 <= length - 3 and jx-1 >= 2 and input[ix+1][jx-1] == 'M':
                if input[ix+2][jx-2] == 'A' and input[ix+3][jx-3] == 'S':
                    words += 1

print(words)