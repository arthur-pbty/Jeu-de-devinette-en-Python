import tkinter as tk
import random

# Fonction pour vérifier le nombre entré par le joueur
def check_guess():
    user_guess = int(guess_entry.get())
    if user_guess == secret_number:
        result_label.config(text="Bravo ! Vous avez deviné le nombre.")
    elif user_guess < secret_number:
        result_label.config(text="Trop bas. Essayez encore.")
    else:
        result_label.config(text="Trop haut. Essayez encore.")

# Fonction pour démarrer un nouveau jeu
def new_game():
    global secret_number
    secret_number = random.randint(1, 100)
    result_label.config(text="Nouveau jeu a commencé. Devinez le nombre entre 1 et 100.")

# Création de la fenêtre principale
window = tk.Tk()
window.title("Devinez le nombre")

# Génération d'un nombre secret aléatoire
secret_number = random.randint(1, 100)

# Création des widgets
header_label = tk.Label(window, text="Devinez le nombre entre 1 et 100.")
guess_label = tk.Label(window, text="Entrez votre devinette :")
guess_entry = tk.Entry(window)
check_button = tk.Button(window, text="Vérifier", command=check_guess)
result_label = tk.Label(window, text="Bonne chance !")
new_game_button = tk.Button(window, text="Nouveau jeu", command=new_game)

# Placement des widgets dans la fenêtre
header_label.pack()
guess_label.pack()
guess_entry.pack()
check_button.pack()
result_label.pack()
new_game_button.pack()

# Démarrer la boucle principale de l'interface graphique
window.mainloop()
