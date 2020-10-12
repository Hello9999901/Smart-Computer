import random
import tkinter as tk


action = tk.Tk()

action.title("Smart Computer")

def generate():
    tk.Label(action, text="\t\t\t\t\t\t\t\t", font = "Arial 25").grid(row=2, sticky=tk.N)
    word_list = []
    with open('/Users/byranhuang/Documents/words.txt') as f:  # or whatever the wordlist is saved as
        for line in f.readlines():
            index, word = line.strip().split('\t')
            word_list.append(word)
    x = (" ")
    x = (" ").join([word_list[random.randrange(0, len(word_list))] for i in range(4)])
    tk.Label(action, text=x, font = "Arial 25").grid(row=2, sticky=tk.N)

tk.Label(action, text="Smart Computer", font = "Arial 50").grid(row=0, sticky=tk.N)
tk.Button(action, text='Talk to Smart Computer', font = "Arial 25", command = generate).grid(row=1, column=0, sticky=tk.N)

tk.mainloop()