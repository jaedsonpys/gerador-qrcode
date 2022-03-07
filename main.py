from tkinter import *
from PIL import ImageTk, Image
from generator import make_qrcode


def load_image(filepath: str = './default_qrcode.png'):
    image = Image.open(filepath)
    resize_image = image.resize((400, 400))
    return ImageTk.PhotoImage(resize_image)


def gen_qrcode() -> str:
    global text_qrcode
    global image_label

    text = text_qrcode.get()
    filename = make_qrcode(text)

    img = load_image(filename)
    image_label.configure(image=img)
    image_label.image = img
    return filename


root = Tk()
root.title('QRCode generator')
root.geometry('500x500')
root.resizable(0, 0)

root.configure(bg='white')

text_frame = Frame(root, bg='white')
text_frame.grid(column=0, row=1, pady=10, padx=10)

button = Button(text_frame, text='Gerar QR Code', bg='white', command=gen_qrcode)
button.grid(column=0, row=1, padx=10)

text_qrcode = Entry(text_frame, width=30)
text_qrcode.grid(column=1, row=1, ipady=3)

image_frame = Frame(root, bg='white')
image_frame.grid(row=2, column=0)

img = load_image()
image_label = Label(image_frame, image=img)
image_label.grid(row=0, column=0, pady=10, padx=40)

root.mainloop()