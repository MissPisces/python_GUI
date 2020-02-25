# 导入tkinter库
import tkinter
import tkinter.filedialog

# 创建主窗口对象
root = tkinter.Tk()

# 设置窗口大小
root.geometry('500x500')


# 定义函数
def filename():
    path = tkinter.filedialog.askopenfilename(initialdir='/usr')
    print(path)


# 添加按钮
but = tkinter.Button(root, text='文件名', command=filename)
but.pack()

# 将主窗口对象加入消息循环中
root.mainloop()
