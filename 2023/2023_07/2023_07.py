
with open('input.txt') as input:
    input = [c.strip('\n') for c in input]

strength = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']
strength2 = ['A','K','Q','T','9','8','7','6','5','4','3','2','J']
ranking = []
five, four, fullhouse, three, twopair, pair, other = [], [], [], [], [], [], []
for i in input:
    rest, winnings = i.split(' ')
    cards = [c for c in rest]
    score = 0
    power = dict()
    for idx, card in enumerate(cards):
        badness = strength2.index(card) + 1
        relative = 10**((len(cards)-idx-1)*2)
        score += relative * badness
        if card in power:
            power[card] += 1
        else:
            power[card] = 1

    max_value = [0,0, ' ']
    if 'J' in power.keys():
        print('before', power)
        js = power['J']
        if js != 5:
            for i in power.keys():
                if i != 'J':
                    if power[i] == max_value[1] and strength2.index(i) < max_value[0]:
                        max_value = [strength2.index(i), power[i], i]
                    elif power[i] > max_value[1]:
                        max_value = [strength2.index(i), power[i], i]
        # print(max_value)
    if max_value[2] != ' ':
        power[max_value[2]] += js
        print('during', power)
        del power['J']
        print('after', power)

    if 5 in power.values():
        five.append([score, cards, winnings, 'five'])
    elif 4 in power.values():
        four.append([score, cards, winnings, 'four'])
    elif 3 in power.values() and 2 in power.values():
        fullhouse.append([score, cards, winnings, 'fullhouse'])
    elif 3 in power.values():
        three.append([score, cards, winnings, 'three'])
    elif 2 in power.values() and len(power) == 3:
        twopair.append([score, cards, winnings, 'twopair'])
    elif 2 in power.values():
        pair.append([score, cards, winnings,  'onepair'])
    else:
        other.append([score, cards, winnings, 'high'])

print('lengths')
five.sort(key=lambda x: int(x[0]), reverse = True)
print(len(five))
four.sort(key=lambda x: int(x[0]), reverse = True)
print(len(four))
fullhouse.sort(key=lambda x: int(x[0]), reverse = True)
print(len(fullhouse))
three.sort(key=lambda x: int(x[0]), reverse = True)
print(len(three))
twopair.sort(key=lambda x: int(x[0]), reverse = True)
print(len(twopair))
pair.sort(key=lambda x: int(x[0]), reverse = True)
print(len(pair))
other.sort(key=lambda x: int(x[0]), reverse = True)
print(len(other))

ranking = other + pair + twopair + three + fullhouse + four + five
print(len(ranking))
total1 = 0
for index, rank in enumerate(ranking):
    # print(index+1, rank[2], rank)
    total1 += (index+1) * int(rank[2])

print(total1)

    
    



