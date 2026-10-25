# Monte Carlo прогноз для ЛР9: скільки спринтів потрібно, щоб закрити залишок points.
# Запуск: python3 forecast.py 220 21 17 26 14 23 6 28 12 22 25 18 9
# Перше число це залишок points, далі velocity спринтів, з яких тягнемо випадково.
import math
import random
import sys

RUNS = 10000
SEED = 2026  # фіксоване зерно, щоб прогін можна було повторити


def one_run(remaining, history, rng):
    sprints = 0
    while remaining > 0:
        remaining -= rng.choice(history)
        sprints += 1
    return sprints


def percentile(results, share):
    # найменша кількість спринтів, на якій накопичена частка прогонів досягла share
    ordered = sorted(results)
    return ordered[math.ceil(share * len(ordered)) - 1]


def main():
    remaining = int(sys.argv[1])
    history = [int(x) for x in sys.argv[2:]]
    if remaining > 0 and max(history) <= 0:
        sys.exit("усі спринти з нулем: залишок ніколи не закриється")
    rng = random.Random(SEED)
    results = [one_run(remaining, history, rng) for _ in range(RUNS)]
    print("прогонів", RUNS, "P50", percentile(results, 0.50), "P85", percentile(results, 0.85))


main()
