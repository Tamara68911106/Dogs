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
            img.thumbnail((300,300))
            img = ImageTk.PhotoImage(img)
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

window.mainloop()