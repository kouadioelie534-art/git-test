from main import rand_generator,display_numbers

#petit algo qui utilise rand_generator et display_numbers de façon intéressante

def rand_average(n:int):
    total = 0
    count = 0
    for num in rand_generator(n):
        total += num
        count += 1
    average = total / count if count > 0 else 0
    display_numbers()  # Afficher les nombres générés
    return average
