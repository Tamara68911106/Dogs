from tkinter import*
from tkinter import ttk
from tkinter import messagebox as mb
import requests # что загрузать из инета изображения
from PIL import Image, ImageTk  # чтобы обрабатывать
from io import BytesIO # чтобы обрабатывать картинку


def get_dog_image():
    try:
        response= requests.get("https://dog.ceo/api/breeds/image/random")
        response.raise_for_status()
        data = response.json()
        return data ['message']
    except Exception  as e:
        mb.showerror("Ошибка", f"Возникла ошибка при запросе к API {e}")
        return None # если ошибка  - возвращаем пустоту(None)

def show_image():
    image_url=get_dog_image()#ссылка на картинку, к-ю возвращает в формате json
    if image_url:
        try:
            response = requests.get(image_url, stream=True)
            response.raise_for_status()
            img_data = BytesIO(response.content)# с помощью байт загружаем респонсконт
            img = Image.open(img_data)
            img_size =(int(width_spinbox.get()), int(height_spinbox.get())) # с помощью int делаем целове число.
            img.thumbnail(img_size)
            img = ImageTk.PhotoImage(img)
            #new_window = Toplevel(window)
            #new_window.title('случайное изображение')
            tab = ttk.Frame(notebook) #tab - закладка
            notebook.add(tab, text = f'Картинка №{notebook.index('end')+1}')# add - добавить
            lb = ttk.Label(tab, image=img)
            lb.pack(padx=10, pady=10)
            lb.image = img


            label.config(image=img)
            label.image=img
        except Exception as e:
            mb.showerror("Ошибка", f"Возникла ошибка при загрузке изображения {e}")# если что-то пойдет не так - выдаст ошибку

    progress.stop()

def prog():  # строка, отображающая загрузку
    progress['value']=0
    progress.start(30)
    window.after(3000, show_image)

window = Tk()
window.title("Картинки с собачками")
window.geometry("360x420")


label = ttk.Label()
label.pack(pady=10)


button =ttk.Button(text="загрузить изображение", command=prog)
button.pack(pady=10)

progress = ttk.Progressbar(mode="determinate", length=300)
progress.pack(pady=10)

width_label=ttk.Label(text = "Ширина:")
width_label.pack(side='left', padx=(10,0)) #у виджетов ttk другие параметры, side left - прижато слево метка. (10.0) справа будет 10 пикселей, слева-0
width_spinbox= ttk.Spinbox(from_=200, to=500, increment=50,width=5)
width_spinbox.pack(side='left', padx=(0,10))

height_label = ttk.Label(text='Высота:')
height_label.pack(side='left', padx=(0,10))
height_spinbox=ttk.Spinbox(from_=200, to=500, increment=50,width=5)
height_spinbox.pack(side='left', padx=(0,10))

top_level_window = Toplevel(window)
top_level_window.title("Изображение собакенов")

notebook = ttk.Notebook(top_level_window)
notebook.pack(expand = True, fill='both', padx=10, pady=10) #чтобы окно было на все пространство

window.mainloop()