import numpy as np

input = open("Q7_input.txt", "r").readlines()

hand_bid = []
for line in input:
    cards_str, bid_str = line.split('\n')[0].split(' ')
    cards = []
    for c in cards_str:
        if c.isnumeric() : cards.append(int(c))
        if c == 'T': cards.append(10)
        if c == 'J': cards.append(11)
        if c == 'Q': cards.append(12)
        if c == 'K': cards.append(13)
        if c == 'A': cards.append(14)        
    hand_bid.append([cards, int(bid_str)])
#print(hand_bid)

def find_type(cards) : 
    [a,b,c, d, e] = sorted(cards)
    if a==e : return 6
    if a==d or b == e : return 5 #four same cards
    if (a==c and d==e) or (a==b and c==e): return 4  #house
    if a==c or b==d or c==e : return 3 #brelan
    if len(set(cards))==3: return 2 #2 pairs
    if len(set(cards))==4: return 1
    return 0

type_hand_bid = [[[find_type(hand)] + hand, bid] for [hand, bid] in hand_bid ]  #first number in hand is the type
type_hand_bid.sort()
print(np.sum([(i+1)*hand[1] for i,hand in enumerate(type_hand_bid)]))
    