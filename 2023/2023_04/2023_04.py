import timeit

start = timeit.default_timer()

with open('input.txt') as input:
    cards = [c.strip('\n') for c in input]

total1 = 0
total2 = 0
cardcounts = [1]
for x in range(len(cards)-1):
    cardcounts.append(1)

for idx, line in enumerate(cards):
    card, numbers = line.split(":")
    winners, candidates = numbers.split("|")
    winners = winners.strip(' ').split(' ')
    candidates = candidates.strip(' ').split(' ')
    while("" in winners):
        winners.remove("")
    while("" in candidates):
        candidates.remove("")
    score = 0
    copies = 0
    for winner in winners:
        if winner in candidates and score == 0:
            copies = 1
            score += 1
        elif winner in candidates:
            copies += 1
            score = score*2
    for copy in range(copies):
        cardcounts[idx + copy + 1] += cardcounts[idx]
    total1 += score

print(cardcounts)
total2 = sum(cardcounts)



print(total1, total2)

stop = timeit.default_timer()
execution_time = stop - start

print("Program Executed in "+str(execution_time)) # It returns time in seconds



