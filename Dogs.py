from tkinter import*
from tkinter import messagebox as mb
import requests # что загрузать из инета изображения
from PIL import Image, ImageTk  # чтобы обрабатывать
from io import BytesIo # чтобы обрабатывать картинку


def get_dog_image():
    try:
        response= requests.get("https://dog.ceo/api/breeds/image/random")
        response.raise_for_status()
        data = response.json()
        return data('message')
    except Exception  as e:
        mb.showerror("Ошибка", f"Возникла ошибка при запросе к API {e}")
        return None # если ошибка  - возвращаем пустоту(None)

def show_image():
    image_url=get_dog_image()#ссылка на картинку, к-ю возвращает в формате json
    if image_url:
        try:
            response = requests.get(image_url, stream=True)
            response.raise_for_status()
            img_data = BytesIo(response.content)# с помощью байт загружаем респонсконт
            img = Image.open(img_data)
            img.thumbnail((300,300))
            img = ImageTk.PhotoImage(img)
            label.config(image=img)
            label.image=img
        except Exception as e:
            mb.showerror("Ошибка", f"Возникла ошибка при загрузке изображения {e}")# если что-то пойдет не так - выдаст ошибку

window = Tk()
window.title("Картинки с собачками")
window.geomety("360x420")


label = Label()
label.pack(pady=10)


button = Button(text="загрузить изогражения", command=show_image)
button.pack(pady=10)