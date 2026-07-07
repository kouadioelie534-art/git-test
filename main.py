from random import randint

def rand_generator(n:int):
    for _ in range(n):
        yield randint(1, 100)

#testons
rand_gen = rand_generator(10)
print(list(rand_gen)) 