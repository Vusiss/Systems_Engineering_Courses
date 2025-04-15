import tkinter as tk

root = tk.Tk()
root.title("Konfiguracja wykresów")



entry = tk.Entry(root)
entry.pack()

def read_entry():
    value = entry.get()
    print(f"Wartość wprowadzona przez użytkownika to: {value}")

button = tk.Button(root, text="Odczytaj wartość", command=read_entry)
button.pack()

root.mainloop()