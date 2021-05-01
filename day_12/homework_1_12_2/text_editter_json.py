# Доработайте текстовый редактор.
# Сделайте так, чтобы при сохранении данных в выбранный файл
# редактор записывал в специальный файл настроек settings.json информацию о том, куда в последний раз были сохранены данные.
# Файл настроек должен иметь формат json-файла (словаря). Например: {'file_name':'C:/Users/ozon/p18/13/text_editor.txt'}
# Сделайте так, чтобы при запуске приложения текстовый редактор автоматически находил файл settings.json и
# подгружал в текстовый редактор последние сохраненные пользователем данные.

import tkinter as tk
from tkinter.filedialog import asksaveasfilename
from tkinter.filedialog import askopenfilename
import json

text = ''
with open('settings.json') as settings_file:
    data = json.load(settings_file)
    if data['file_name'] != '':
        with open(data['file_name']) as text_file:
           text = text_file.read()

window = tk.Tk()
window.title('Текстовый редактор')

frame_top = tk.Frame(window, height=300, width=300)
frame_top.pack(fill=tk.BOTH, expand=True)

# Фрейм с основным полем ввода текста
text_field = tk.Text(frame_top)
text_field.insert(1.0, text)
text_field.pack(fill=tk.BOTH, expand=True)

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

    with open('settings.json', 'w') as settings_file:
        json.dump({'file_name': file_path}, settings_file)

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
