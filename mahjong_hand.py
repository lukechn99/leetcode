# PALANTIR

# tiles1 = "11133555"
# tiles2 = "111333555"
# tiles3 = "00000111"
# tiles4 = "13233121"
# tiles5 = "11223344555"
# tiles6 = "99999999"
# tiles7 = "999999999"
# tiles8 = "9"
# tiles9 = "99"
# tiles10 = "000022"
# tiles11 = "888889"
# tiles12 = "889"
# tiles13 = "88888844"
# tiles14 = "77777777777777"
# tiles15 = "1111111"
# tiles16 = "1111122222"

def complete(hand):
    count = {}
    for piece in hand:
        if piece in count:
            count[piece] += 1
        else:
            count[piece] = 1
    # 1 instance -> False
    # (n - 2) divisible 3
    # pair
    # not more than 1 pair
    pair = 0
    # 6
    for tile in count.keys():
        if count[tile] == 1:
            print(False)
            return False
        elif (count[tile] - 2) % 3 == 0:
            pair += 1
        elif not (count[tile] % 3 == 0) and count[tile] % 2 == 0:
            pair += count[tile] / 2
    print(pair == 1)
    return (pair == 1)
    


