# 1. Climbing Algorithm（Hill Climbing） - 求最大值 f(x) = -x^2 + 5x
import random

def hill_climbing():
    current_x = random.uniform(0, 5)
    step = 0.01
    for _ in range(1000):
        next_x = current_x + random.choice([-step, step])
        if next_x < 0 or next_x > 5:
            continue
        if f(next_x) > f(current_x):
            current_x = next_x
    return current_x, f(current_x)

def f(x):
    return -x**2 + 5*x

print("Hill Climbing:", hill_climbing())

