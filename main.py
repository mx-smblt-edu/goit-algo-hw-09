from timeit import timeit
import rich
from rich.table import Table
from find_coins_greedy import find_coins_greedy
from find_min_coins import find_min_coins

AMOUNT_KEY = 'amount'
FIND_COINS_GREEDY_TIME_KEY = 'find_coins_greedy_time'
FIND_MIN_COINS_TIME_KEY = 'find_min_coins_time'
FIND_COINS_GREEDY_RESULT_KEY = 'find_coins_greedy_result'
FIND_MIN_COINS_RESULT_KEY = 'find_min_coins_result'


def compare_performance(coins: list[int], amounts: list[int]):
    results = []
    for amount in amounts:
        find_coins_greedy_result = find_coins_greedy(coins, amount)
        find_coins_greedy_time = timeit(lambda: find_coins_greedy(coins, amount), number=1000)

        find_min_coins_result = find_min_coins(coins, amount)
        find_min_coins_time = timeit(lambda: find_min_coins(coins, amount), number=1000)

        results.append(
            {
                AMOUNT_KEY: str(amount),
                FIND_COINS_GREEDY_RESULT_KEY: find_coins_greedy_result,
                FIND_COINS_GREEDY_TIME_KEY: str(round(find_coins_greedy_time * 1000, 5)),
                FIND_MIN_COINS_RESULT_KEY: find_min_coins_result,
                FIND_MIN_COINS_TIME_KEY: str(round(find_min_coins_time * 1000, 5))
            }
        )

    return results


def print_result(results):
    print("Results:")
    table_result = Table(show_header=True)
    table_result.add_column("Amount", justify="center", no_wrap=True)
    table_result.add_column("Greedy (count)", justify="left", no_wrap=True)
    table_result.add_column("DP (count)", justify="left", no_wrap=True)
    for item in results:
        table_result.add_row(
            item[AMOUNT_KEY],
            str(item[FIND_COINS_GREEDY_RESULT_KEY]),
            str(item[FIND_MIN_COINS_RESULT_KEY])
        )
    rich.print(table_result)


def print_times(results):
    print("Times:")
    table_time = Table(show_header=True)
    table_time.add_column("Amount", justify="center", no_wrap=True)
    table_time.add_column("Greedy time (ms)", justify="right", no_wrap=True)
    table_time.add_column("DP time (ms)", justify="right", no_wrap=True)
    for item in results:
        table_time.add_row(
            item[AMOUNT_KEY],
            item[FIND_COINS_GREEDY_TIME_KEY],
            item[FIND_MIN_COINS_TIME_KEY]
        )
    rich.print(table_time)


def main():
    coins = [50, 25, 10, 5, 2, 1]
    amounts = [3, 7, 8, 9, 10, 100, 256, 512, 1024, 2048, 4096]
    results = compare_performance(coins, amounts)
    print_result(results)
    print_times(results)


if __name__ == '__main__':
    main()
