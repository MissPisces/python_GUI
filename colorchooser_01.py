# 导入tkinter库
import tkinter
import tkinter.colorchooser

# 创建主窗口对象
root = tkinter.Tk()

# 设置窗口大小
root.geometry('500x500')


# 定义函数
def color():
    result = tkinter.colorchooser.askcolor(color='red')
    print(result)
    # 设置背景颜色
    root['bg'] = result[1]


# 添加按钮
but = tkinter.Button(root, text='选择颜色', command=color)
but.pack()

# 将主窗口对象加入消息循环中
root.mainloop()
