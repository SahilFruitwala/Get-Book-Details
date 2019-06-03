import tkinter as tk
from tkinter import font
import PIL.Image
import PIL.ImageTk
from getData import GetData
import urllib
import io

HEIGHT = 400
WIDTH = 500

def show_data(entry):
    bookName = entry.get().strip()
    if bookName == '':
        entry.delete(0, tk.END)
        entry.insert(0, '')
    else:
        book = GetData(bookName)
        book_data = book.parsed_data()
        print(book_data)
        if type(book_data) == tuple:
            raw_data = urllib.request.urlopen(str(book_data[5])).read()
            im = PIL.Image.open(io.BytesIO(raw_data))
            image = PIL.ImageTk.PhotoImage(im)
            label1.configure(image=image)
            label['text'] = "Book : " + str(book_data[0]) + '\n' + "Author : " + str(book_data[1]) + '\n' + "Published Year : " + str(book_data[2]) + '\n' + "Rating : " + str(book_data[3]) + '\n' + "Total Reviews : " + str(book_data[4])
            label1.photo = image
        else :
            label['text'] = book_data
        entry.delete(0, tk.END)
        entry.insert(0, bookName)

root = tk.Tk()
root.title('Get Book Data')

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

bg_img = PIL.Image.open("images/background.jpg")
background_image = PIL.ImageTk.PhotoImage(bg_img)
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

upper_frame = tk.Frame(root, bg='#80C1FF', bd=3)
upper_frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(upper_frame, font=('Courier',12))
entry.focus_set()
entry.place(relwidth=0.65, relheight=1)
entry.bind("<Return>", (lambda event: show_data(entry)))
# entry.pack(side='left')
# entry.grid(row=0, column=1)

button = tk.Button(upper_frame, text="Search", font=('Courier',12), command=lambda: show_data(entry))
button.place(relx=0.7, relwidth=0.3, relheight=1)
# button.pack(side='right')
# button.grid(row=0, column=2)

lower_frame = tk.Frame(root, bg='#80C1FF', bd=3)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier',12), anchor='nw', justify='left', wraplength=200)
label.place(relwidth=0.6, relheight=1)
# label.pack(side='left')
# label.grid(row=0, column=0)

label1 = tk.Label(lower_frame,anchor='nw')
label1.place(relx=0.63,relwidth=0.4, relheight=1)

root.mainloop()
