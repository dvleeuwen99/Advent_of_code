
with open('input.txt') as input:
    input = [c.strip('\n') for c in input]

changes = list()
for idx,line in enumerate(input):
    if line == '':
        changes.append(idx)

seeds = input[:changes[0]]
soil = input[changes[0]+2:changes[1]]

fertilizer = input[changes[1]+2:changes[2]]

water = input[changes[2]+2:changes[3]]

light = input[changes[3]+2:changes[4]]

temperature = input[changes[4]+2:changes[5]]

humidity = input[changes[5]+2:changes[6]]

location = input[changes[6]+2:]

seeds = seeds[0][7:].split(' ')

#part 1

locations = list()

for seed in seeds:
    value = int(seed)
    for line in soil:
        dest, start, length = line.split(" ")
        dest, start, length = int(dest), int(start), int(length)
        if value >= start and value <= start + length:
            value += dest-start
            break
    for line in fertilizer:
        dest, start, length = line.split(" ")
        dest, start, length = int(dest), int(start), int(length)
        if value >= start and value <= start + length:
            value += dest-start
            break
    for line in water:
        dest, start, length = line.split(" ")
        dest, start, length = int(dest), int(start), int(length)
        if value >= start and value <= start + length:
            value += dest-start
            break
    for line in light:
        dest, start, length = line.split(" ")
        dest, start, length = int(dest), int(start), int(length)
        if value >= start and value <= start + length:
            value += dest-start
            break
    for line in temperature:
        dest, start, length = line.split(" ")
        dest, start, length = int(dest), int(start), int(length)
        if value >= start and value <= start + length:
            value += dest-start
            break
    for line in humidity:
        dest, start, length = line.split(" ")
        dest, start, length = int(dest), int(start), int(length)
        if value >= start and value <= start + length:
            value += dest-start
            break
    for line in location:
        dest, start, length = line.split(" ")
        dest, start, length = int(dest), int(start), int(length)
        if value >= start and value <= start + length:
            value += dest-start
            break
    
    locations.append(value)

total1 = min(locations)
print(total1)

#part 2
def ranges(seeds):
    seed_ranges = []
    for i in range(round(len(seeds)/2)):
        seed_ranges.append([int(seeds[2*i]), int(seeds[2*i]) + int(seeds[2*i+1]) - 1])
    new_seed_ranges = [seed_ranges[0]]
    for i in seed_ranges[1:]:
        for j in new_seed_ranges:
            if i[0] >= j[0] and i[1] <= j[1]:
                continue
            elif i[0] <= j[1] and i[1] >= j[1]:
                new_seed_ranges.remove(j)
                j[1] = i[1]
                new_seed_ranges.append(j)
            elif i[1] >= j[0] and i[0] <= j[0]:
                new_seed_ranges.remove(j)
                j[0] = i[1]
                new_seed_ranges.append(j) 
        new_seed_ranges.append(i)
    return new_seed_ranges

def new_ranges(ranges):
    new_ranges = [ranges[0]]
    for i in ranges[1:]:
        new = False
        for j in new_ranges:
            if i[0] >= j[0] and i[1] <= j[1]: #falls entirely into range
                new = True
            elif i[0] <= j[1] and i[1] > j[1]: #only last part overlaps
                new_ranges.remove(j)
                k = [j[0], i[1]]
                new_ranges.append(k)
                new = True
            elif i[1] >= j[0] and i[0] < j[0]: #only first part overlaps
                new_ranges.remove(j)
                k = [i[0], j[1]]
                new_ranges.append(k)
                new = True
        if new == False:
            new_ranges.append(i)
            
    return new_ranges

def switching(ranges, nextobject):
    new_ranges = []
    for seed in ranges:
        new = False
        begin = seed[0]
        eind = seed[1]
        for line in nextobject:
            dest, start, length = map(int, line.split(" "))
            if begin >= start and eind < start + length: #entire range falls in new range
                print('case 1', begin, eind)
                new = True
                new_ranges.append([begin + dest - start, eind + dest - start])
            elif begin >= start and begin < start + length: #only first part falls in new range, rest stays the same
                print('case 2', begin, eind)
                new = True
                new_ranges.append([begin + dest - start, dest + length])
                ranges.append([start + length, eind])
            elif eind >= start and eind <= start + length: #only last part falls in new range, rest stays the same
                print('case 3', begin, eind)
                new = True
                ranges.append([begin, start - 1])
                new_ranges.append([dest, eind + dest - start])
        if new == False:
            new_ranges.append([begin,eind])
                
    return new_ranges

seed_ranges = ranges(seeds)
print('seeds', seed_ranges)
print('next', soil)
soil_ranges = switching(seed_ranges, soil)
print('progress', soil_ranges)
soil_ranges = new_ranges(soil_ranges)
print('soil', soil_ranges)
print('next', fertilizer)
fert_ranges = switching(soil_ranges, fertilizer)
print('progress', fert_ranges)
fert_ranges = new_ranges(fert_ranges)
print('fert', fert_ranges)
print('next', water)
water_ranges = switching(fert_ranges, water)
print('progress', water_ranges)
water_ranges = new_ranges(water_ranges)
print('water', water_ranges)
print('next', light)
light_ranges = switching(water_ranges, light)
print('progress', light_ranges)
light_ranges = new_ranges(light_ranges)
print('light', light_ranges)
print('next', temperature)
temperature_ranges = switching(light_ranges, temperature)
print('progress', temperature_ranges)
temperature_ranges = new_ranges(temperature_ranges)
print('temp', temperature_ranges)
print('next', humidity)
humidity_ranges = switching(temperature_ranges, humidity)
print('progress', humidity_ranges)
humidity_ranges = new_ranges(humidity_ranges)
print('humidity', humidity_ranges)
print('next', location)
location_ranges = switching(humidity_ranges, location)
print('progress', location_ranges)
location_ranges = new_ranges(location_ranges)
print('location', location_ranges)

total2 = 100000000000000000000000
for loc in location_ranges:
    total2 = min(loc[0], total2)
print(total2)

            

    
        




