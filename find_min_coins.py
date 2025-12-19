def find_min_coins(coins: list[int], amount: int):
    table = [float('inf')] * (amount + 1)
    table[0] = 0
    coin_used = [0] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin and table[i - coin] + 1 < table[i]:
                table[i] = table[i - coin] + 1
                coin_used[i] = coin

    result = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin

    return result
