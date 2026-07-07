from main import rand_generator

#petit algo qui utilise rand_generator de façon interessante
def rand_sum(n:int):
    total = 0
    for num in rand_generator(n):
        total += num
    return total

#testons
result = rand_sum(10)
print(result)