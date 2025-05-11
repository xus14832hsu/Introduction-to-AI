# 4. Genetic Algorithm - 解最大化 f(x) = x^2（x 為整數）
import random

def fitness(x): return x**2

def mutate(x): return x + random.choice([-1, 1])

def crossover(x, y): return (x + y) // 2

def genetic_algorithm():
    population = [random.randint(0, 31) for _ in range(10)]
    for _ in range(100):
        population = sorted(population, key=fitness, reverse=True)
        next_gen = population[:2]
        while len(next_gen) < 10:
            parent1, parent2 = random.sample(population[:5], 2)
            child = mutate(crossover(parent1, parent2))
            next_gen.append(max(0, min(31, child)))
        population = next_gen
    best = max(population, key=fitness)
    return best, fitness(best)

print("Genetic Algorithm Best:", genetic_algorithm())

