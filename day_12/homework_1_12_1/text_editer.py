# С помощью tkinter создайте простой текстовый редактор, в котором есть:
# 1. Поле редактирования текста;
# 2. Кнопка сохранения текста в файл - при ее нажатии должен вызываться диалог выбора имени файла. Все
# данные из поля редактирования текста должны сохраняться в выбранный файл;
# 3. Кнопка загрузки текста из файла - при ее нажатии должен вызываться диалог выбора имени файла. После
# выбора файла поле редактирования текста должно очищаться и в него должны записываться данные из
# выбранного файла.

import tkinter as tk
from tkinter.filedialog import asksaveasfilename
from tkinter.filedialog import askopenfilename

window = tk.Tk()
window.title('Текстовый редактор')

frame_top = tk.Frame(window)
frame_top.pack()

# Фрейм с основным полем ввода текста
text_field = tk.Text(frame_top, height=20, width=100)
text_field.pack()

# Фрейм с кнопками
frame_bottom = tk.Frame(window)
btn_save = tk.Button(master=frame_bottom, text="Сохранить")
btn_save.pack(fill=tk.X, side=tk.RIGHT)

btn_load = tk.Button(master=frame_bottom, text="Загрузить")
btn_load.pack(fill=tk.X, side=tk.LEFT)
frame_bottom.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)


def save_data(event):
    file_path = asksaveasfilename(defaultextension='txt', filetypes=[('Text Files', '*.txt'),
                                                                     ('All files', '*.*')])
    # Если ничего не выбрано отжать кнопку
    if not file_path: return 'break'

    # Открыть файл на запись
    with open(file_path, 'w') as output_file:
        # Взять содержимое текстового поля и записать в файл
        output_file.write(text_field.get("1.0", "end"))

    return 'break'


btn_save.bind('<Button-1>', save_data)


def load_data(event):
    file_path = askopenfilename(defaultextension='txt', filetypes=[('Text Files', '*.txt'),
                                                                   ('All files', '*.*')])

    # Проверяем найден ли вообще файл
    if not file_path: return 'break'  # отжимает кнопку

    # Очищаем текстовое поле если пользователь что-то ввел до загрузки
    text_field.delete(1.0, tk.END)

    # Откроем файл на чтение
    with open(file_path, 'r') as input_file:
        # Получим весь файл и содержимое вставляем в текстовое поле
        text_field.insert(tk.END, input_file.read())

    return 'break'


btn_load.bind('<Button-1>', load_data)

window.mainloop()
