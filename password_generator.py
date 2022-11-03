from random import randint, choice
import string
from tkinter import *


def generate_password():
    password_min = 6
    password_max = 15
    all_chars = string.ascii_letters + string.punctuation + string.digits
    password = "".join(choice(all_chars) for _ in range(randint(password_min, password_max)))
    password_entry.delete(0, END)
    password_entry.insert(0, password)


def affichage():
    window.geometry("1920x1080")


# Personnalisation de notre fenêtre
window = Tk()
window.title("Générateur de mot passe")
window.geometry("1280x800")
window.iconbitmap("../image/totem_gigachad.ico")
window.minsize(800, 600)
window.config(background='#4065A4')

# Boite frame principal
frame = Frame(window, bg='#4065A4')

# Insertion d'une image
width = 412
height = 412
image = PhotoImage(file="../image/password-icon.png").zoom(30).subsample(40)
canvas = Canvas(frame, width=width, height=height, bg='#4065A4', bd=0, highlightthickness=0)
canvas.create_image(width/2, height/2, image=image)
canvas.grid(row=0, column=0, sticky=W)

# Boite frame de droite
right_frame = Frame(frame, bg='#4065A4')

# texte du mot de passe
label_title = Label(right_frame, text="Mot de passe", font=("Helvetica", 20), bg='#4065A4', fg='white')
label_title.pack(expand=YES)
right_frame.grid(row=0, column=1, sticky=W)

# Création d'une entrer de texte pour un mot de passe
password_entry = Entry(right_frame, font=("Helvetica", 20), bg='#4065A4', fg='white')
password_entry.pack(expand=YES)

# Création d'un bouton
generate_password_button = Button(right_frame, text="Générer", font=("Helvetica", 20), bg='#4065A4', fg='white',
                                  command=generate_password)
generate_password_button.pack(fill=X, expand=YES)

# Centration de notre boîte pour s'adapter à la taille de la fenêtre
frame.pack(expand=YES)


# création d'une barre de menu
menu_bar = Menu(window)

# Créer un premier menu
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Nouveau", command=generate_password)
file_menu.add_command(label="Quittez", command=window.quit)
file_menu.add_command(label="Affichage", command=affichage)
menu_bar.add_cascade(label="Général", menu=file_menu)


# Configurer pour ajouter notre menu bar
window.config(menu=menu_bar)


# Affichage de la fenêtre
window.mainloop()
