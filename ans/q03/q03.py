NUMBER = 100
cards = []
for i in range(0, NUMBER):
    cards.append(False)
for i in range(2, NUMBER):
    for j in range(i, NUMBER, i):
        j -= 1
        cards[j] = not cards[j]
for i, card in enumerate(cards):
    if card == False:
        print(i+1)