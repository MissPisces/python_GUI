import tkinter

root = tkinter.Tk()
root.geometry('500x500')

canvas = tkinter.Canvas(root, bg='white')
canvas.pack()

#绘制矩形
canvas.create_rectangle(20, 20, 100, 100, fill='red', outline='black')


root.mainloop()
