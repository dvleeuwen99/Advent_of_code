input = []

with open('input.txt', 'r') as file:
    for line in file:
        # process each line
        input.append((line.strip()))

words = 0
length = len(input)
for ix, line in enumerate(input):
    for jx, j in enumerate(line):
        if ix <= length - 2 and ix >= 1 and jx <= length - 2 and jx >= 1:
            if input[ix][jx] == 'A':
                if input[ix-1][jx-1]=='M' and input[ix-1][jx+1]=='M' and input[ix+1][jx+1]=='S' and input[ix+1][jx-1]=='S':
                    words += 1
                elif input[ix-1][jx-1]=='S' and input[ix-1][jx+1]=='S' and input[ix+1][jx+1]=='M' and input[ix+1][jx-1]=='M':
                    words += 1
                elif input[ix-1][jx-1]=='M' and input[ix-1][jx+1]=='S' and input[ix+1][jx+1]=='S' and input[ix+1][jx-1]=='M':
                    words += 1
                elif input[ix-1][jx-1]=='S' and input[ix-1][jx+1]=='M' and input[ix+1][jx+1]=='M' and input[ix+1][jx-1]=='S':
                    words += 1
print(words)