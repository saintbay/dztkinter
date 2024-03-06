import tkinter as tk
import requests
import json
import os

def make_request():
    try:
        id_value = int(id_entry.get())
        response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{id_value}')
        result_text.delete(1.0, tk.END) 
        result_text.insert(tk.END, json.dumps(response.json(), indent=4))
    except ValueError:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Введите корректный ID (целое число).")

def save_result():
    result = result_text.get(1.0, tk.END)
    if result.strip():
        id_value = id_entry.get()
        file_path = os.path.join('saved_results', f'result_{id_value}.json')
        with open(file_path, 'w') as file:
            file.write(result)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"Результат сохранен в {file_path}")
    else:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Нет данных для сохранения.")

app = tk.Tk()
app.title("JSON Placeholder Requester")

id_label = tk.Label(app, text="Введите ID:")
id_entry = tk.Entry(app)
request_button = tk.Button(app, text="Запрос", command=make_request)
result_text = tk.Text(app, height=10, width=50)
save_button = tk.Button(app, text="Сохранить", command=save_result)

id_label.grid(row=0, column=0, padx=10, pady=10)
id_entry.grid(row=0, column=1, padx=10, pady=10)
request_button.grid(row=0, column=2, padx=10, pady=10)
result_text.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
save_button.grid(row=2, column=0, columnspan=3, pady=10)
app.mainloop()
