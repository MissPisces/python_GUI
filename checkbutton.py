import tkinter

root = tkinter.Tk()
root.geometry('500x500')

# 设置显示内容tkinter变量
text = tkinter.StringVar()
# 设置内容
text.set('同意获取')
# 设置勾选与否的值
result = tkinter.IntVar()


# 设置操作Checkbutton的方法
def func():
    print(result.get())


ckb1 = tkinter.Checkbutton(root, bg='red', padx=20, pady=20, text='同意',
                           font=('simhei', 20, 'bold', 'italic'))
ckb1.pack()

# 获取变量名
ckb2 = tkinter.Checkbutton(root, textvariable=text, variable=result, command=func, onvalue='110')
ckb2.pack()

root.mainloop()
