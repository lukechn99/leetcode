def coin(amount, coins):
    '''
    amount: int
    coins: sorted List(int)

    returns minimum number of coins needed
    '''
    if coins[0] > amount:
        pass

    for c in coins:
        if c <= amount:
            max_fit = amount / c
            for i in range(max_fit, 0, -1):
                pass