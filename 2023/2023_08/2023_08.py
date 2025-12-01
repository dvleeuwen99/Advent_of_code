import itertools
with open('input.txt') as input:
    input = [c.strip('\n') for c in input]

route = input[0]
choices = input[2:]
print(route)
choice_dict = {}
for choice in choices:
    start = choice[0:3]
    left = choice[7:10]
    right = choice[12:15]
    choice_dict[start] = [left, right]

part = 'part2'

if part == 'part1':
    location = 'AAA'
    steps = 0
    while location != 'ZZZ':
        print('round')
        for d in route:
            steps += 1
            if d == 'L':
                location = choice_dict[location][0]
            else:
                location = choice_dict[location][1]
            if location == 'ZZZ':
                print('total1', steps)
                break
    
if part == 'part2':
    start_locations = set()
    finish_locations = set()
    for key in choice_dict.keys():
        if key[2] == 'A':
            start_locations.add(key)
        elif key[2] == 'Z':
            finish_locations.add(key)
    steps = []
    for loc in start_locations:
        step = 0
        while loc not in finish_locations:
            for d in route:
                step += 1
                if d == 'L':
                    loc = choice_dict[loc][0]
                else:
                    loc = choice_dict[loc][1]
                if loc in finish_locations:
                    steps.append(step)
                    break
    print(steps)
    
def compute_gcd(x, y):

   while(y):
       x, y = y, x % y
   return x

def compute_lcm(x, y):
   lcm = (x*y)//compute_gcd(x,y)
   return lcm


total_steps = compute_lcm(compute_lcm(compute_lcm(compute_lcm(compute_lcm(steps[0],steps[1]),steps[2]),steps[3]),steps[4]),steps[5])
print(total_steps)