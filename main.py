from random import randint
from tkinter import *

def rand_generator(n:int):
    for _ in range(n):
        yield randint(1, 100)

#testons
rand_gen = rand_generator(10)
print(list(rand_gen)) 

 #ouvrons unse fenêtre tkinter pour afficher les nombres générés
def display_numbers():
    rand_gen = rand_generator(10)
    numbers = list(rand_gen)
    
    root = Tk()
    root.title("Random Numbers")
    
    label = Label(root, text="Generated Random Numbers:")
    label.pack()
    button = Button(root, text="Close", command=root.destroy)
    button.pack()
    
    for num in numbers:
        num_label = Label(root, text=str(num))
        num_label.pack()
    
    root.mainloop()
    
#testons l'affichage
display_numbers()