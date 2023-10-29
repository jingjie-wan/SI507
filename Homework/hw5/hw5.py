def change(amount, coins):
    '''
    amount >= 0
    '''
    if amount == 0: return 0
    elif coins == []: return float('inf')
    else:
        current = coins[0]
        if current > amount: return change(amount, coins[1:])
        else:
            use_it = 1 + change(amount - current, coins)
            lose_it = change(amount, coins[1:])
            return min(use_it, lose_it)

def giveChange(amount, coins):
    '''
    amount >= 0
    '''
    if amount == 0: return [0, []]
    elif coins == []: return [float('inf'), []]
    else:
        current = coins[0]
        if current > amount: return giveChange(amount, coins[1:])
        else:
            use_it = giveChange(amount - current, coins)
            lose_it = giveChange(amount, coins[1:])
            if use_it[0] < lose_it[0]: return [1 + use_it[0], use_it[1] + [current]]
            else: return lose_it