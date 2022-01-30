import random
import tkinter

stats = []


def get_winner(call):
    if random.random() <= (1 / 3):
        throw = "PIEDRA"
    elif (1 / 3) < random.random() <= (2 / 3):
        throw = "TIJERA"
    else:
        throw = "PAPEL"

    if (throw == "PIEDRA" and call == "PAPEL") or (throw == "PAPEL" and call == "TIJERA") \
            or (throw == "TIJERA" and call == "PIEDRA"):
        stats.append('W')
        result = "GANASTE!"
    elif throw == call:
        stats.append('D')
        result = "EMPATE"
    else:
        stats.append('L')
        result = "PERDISTE!"

    global output
    output.config(text="la compu eligio: " + throw + "\n" + result)


def pass_s():
    get_winner("TIJERA")


def pass_r():
    get_winner("PIEDRA")


def pass_p():
    get_winner("PAPEL")


window = tkinter.Tk()
window .title('PIEDRA PAPEL o TIJERA')
window.focus()
scissors = tkinter.Button(window, text="TIJERA", bg="#ff9999", padx=10, pady=20, command=pass_s, width=30)
rock = tkinter.Button(window, text="PIEDRA", bg="#80ff80", padx=10, pady=20, command=pass_r, width=30)
paper = tkinter.Button(window, text="PAPEL", bg="#3399ff", padx=10, pady=20, command=pass_p, width=30)
output = tkinter.Label(window, width=20, fg="red", text="Cual es tu eleccion?")

scissors.pack(side="left")
rock.pack(side="left")
paper.pack(side="left")
output.pack(side="right")
window.mainloop()


for i in stats: print(i, end=" ")
if stats.count('L') > stats.count('W'):
    result = "\nYou loose the series."
elif stats.count('L') == stats.count('W'):
    result = "\nSeries ended in a draw."
else:
    result = "\nYou win the series."

print(result)