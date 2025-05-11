# 3. Monte Carlo 模擬 - 擲骰子模擬出現 6 的機率
import random

def monte_carlo_dice(trials=10000):
    success = 0
    for _ in range(trials):
        if random.randint(1, 6) == 6:
            success += 1
    return success / trials

print("Monte Carlo Dice Success Rate:", monte_carlo_dice())

