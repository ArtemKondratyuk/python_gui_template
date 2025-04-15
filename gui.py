import tkinter as tk
from tkinter import ttk
from mood_generator import load_phrases, get_random_phrase

root = tk.Tk()
root.title("Генератор фраз для поднятия настроения")
root.geometry("600x400")

# Устанавливаем шрифт для меток и кнопок
mood_label = tk.Label(text="Ввыберите настроение:", font=("Arial", 12))
mood_label.pack(pady=10)

# Выпадающий список настроений
mood_options = ["Очень плохое", "Плохое", "Так себе"]
mood_var = tk.StringVar()
mood_combobox = ttk.Combobox(root, textvariable=mood_var, values=mood_options, width=12, font=("Arial", 12), state="readonly")
mood_combobox.pack(pady=10)

# Снятие фокуса с combobox после выбора настроения
def on_combobox_select(event):
# Снимаем фокус с выпадающего списка, чтобы не было выделения
    mood_combobox.selection_clear()

mood_combobox.bind("<<ComboboxSelected>>", on_combobox_select)

# Метка для вывода фразы
phrase_label = tk.Label(root, text="", width=45, height=6, relief="sunken", anchor="center", font=("Arial", 12), wraplength=400, justify="center", padx=7)
phrase_label.pack(pady=20)

def show_phrase():
    mood = mood_var.get()  # Получаем выбранное настроение
    data = load_phrases()
    phrase = get_random_phrase(mood.strip().lower(), data)
    phrase_label.config(text=phrase)

# Кнопка для получения фразы
get_phrase_button = tk.Button(root, text="Получить фразу", command=show_phrase, font=("Arial", 12))
get_phrase_button.pack(pady=10)

# Кнопка для завершения работы программы
def close_app():
    root.quit()

exit_button = tk.Button(root, text="Выход", command=close_app, font=("Arial", 12))
exit_button.pack(pady=10)

root.mainloop()
