# 导入tkinter库 toplevel
import tkinter

# 创建主窗口对象
root = tkinter.Tk()

# 设置窗口大小
root.geometry('500x500')


# 定义新窗口函数
def talk():
    newroot = tkinter.Toplevel()


# 加入组件
but = tkinter.Button(root, text='按钮一', command=talk)

# 摆放组件
but.pack()

# 将主窗口对象加入消息循环中
root.mainloop()
